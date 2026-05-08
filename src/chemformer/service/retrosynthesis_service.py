"""FastAPI service for single-step retrosynthesis using Chemformer.

Reads model configuration from environment variables:
    CHEMFORMER_MODEL  - local path or gs:// URI to .ckpt checkpoint file
    CHEMFORMER_VOCAB  - local path or gs:// URI to bart_vocab.json vocabulary file
    CHEMFORMER_N_BEAMS - (optional) number of beam-search predictions, default 10
    CHEMFORMER_N_GPUS  - (optional) number of GPUs, default 0 (CPU)
    PORT              - (optional) port to listen on, default 8080 (set by Cloud Run)

Run locally:
    CHEMFORMER_MODEL=... CHEMFORMER_VOCAB=... uvicorn \
        chemformer.service.retrosynthesis_service:app --port 8080
"""

import os
import tempfile
from typing import List

import omegaconf as oc
import molbart.utils.data_utils as util
from fastapi import FastAPI, HTTPException
from molbart.constants import CONFIG_DIR
from molbart.data import SynthesisDataModule
from molbart.models import Chemformer
from pydantic import BaseModel


def _resolve_path(uri: str) -> str:
    """Download a gs:// URI to a temp file and return the local path, or pass through."""
    if not uri.startswith("gs://"):
        return uri
    from google.cloud import storage
    bucket_name, blob_path = uri[5:].split("/", 1)
    suffix = os.path.splitext(blob_path)[1]
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    print(f"Downloading {uri} → {tmp.name}")
    storage.Client().bucket(bucket_name).blob(blob_path).download_to_filename(tmp.name)
    return tmp.name


cfg = oc.OmegaConf.load(f"{CONFIG_DIR}/predict.yaml")

cfg.task = "backward_prediction"
cfg.train_mode = "eval"
cfg.model_type = "bart"
cfg.datamodule = None
cfg.n_gpus = int(os.environ.get("CHEMFORMER_N_GPUS", "0"))
cfg.n_beams = int(os.environ.get("CHEMFORMER_N_BEAMS", "10"))
cfg.model_path = _resolve_path(os.environ["CHEMFORMER_MODEL"])
cfg.vocabulary_path = _resolve_path(os.environ["CHEMFORMER_VOCAB"])

chemformer = Chemformer(cfg)

app = FastAPI(title="Chemformer Retrosynthesis", version="1.0")


class RetrosynthesisRequest(BaseModel):
    smiles: str
    n_beams: int = cfg.n_beams


class RetrosynthesisPrediction(BaseModel):
    reaction_smarts: str  # reactants>>product
    reactants_smiles: str
    log_likelihood: float


class RetrosynthesisResponse(BaseModel):
    product_smiles: str
    predictions: List[RetrosynthesisPrediction]


@app.post("/retrosynthesis/predict", response_model=RetrosynthesisResponse)
def predict(request: RetrosynthesisRequest):
    """Predict reactants for a given product SMILES using retrosynthesis (backward prediction)."""
    n_beams = request.n_beams

    datamodule = SynthesisDataModule(
        reactants=[request.smiles],
        products=[request.smiles],
        dataset_path="",
        tokenizer=chemformer.tokenizer,
        batch_size=1,
        max_seq_len=util.DEFAULT_MAX_SEQ_LEN,
        augment_prob=False,
        reverse=True,
    )
    datamodule.setup()

    chemformer.model.num_beams = n_beams
    chemformer.model.n_unique_beams = n_beams

    sampled_smiles, log_lhs, _ = chemformer.predict(dataloader=datamodule.full_dataloader())

    if not sampled_smiles:
        raise HTTPException(status_code=500, detail="Model returned no predictions.")

    beams = sampled_smiles[0]
    lhs = log_lhs[0]

    predictions = [
        RetrosynthesisPrediction(
            reaction_smarts=f"{reactants}>>{request.smiles}",
            reactants_smiles=str(reactants),
            log_likelihood=float(lh),
        )
        for reactants, lh in zip(beams, lhs)
    ]

    return RetrosynthesisResponse(
        product_smiles=request.smiles,
        predictions=predictions,
    )


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "chemformer.service.retrosynthesis_service:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "8080")),
        log_level="info",
        reload=False,
    )
