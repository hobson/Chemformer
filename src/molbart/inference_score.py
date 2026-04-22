import hydra
import molbart.utils.data_utils as util
from molbart.constants import CONFIG_DIR, DATA_DIR, MODELS_DIR
from molbart.models import Chemformer
import omegaconf as oc
from pathlib import Path



# @hydra.main(version_base=None, config_path=CONFIG_DIR, config_name="inference_score")
def main(args, data_path=str(Path(DATA_DIR) / 'seq-to-seq_datasets' / 'mol_opt.pickle')):
    util.seed_everything(args.seed)

    print("Running model inference and scoring.")

    chemformer = Chemformer(args)

    chemformer.score_model(
        n_unique_beams=args.n_unique_beams,
        dataset=args.dataset_part,
        output_scores=args.output_score_data,
        output_sampled_smiles=args.output_sampled_smiles,
    )
    print("Model inference and scoring done.")
    return chemformer


if __name__ == "__main__":
    with hydra.initialize(version_base=None, config_path='config', job_name="hobs_attempting_run_inference_score"):
        cfg = hydra.compose(config_name="inference_score")  # "fine_tune")
    cfg.data_path = str(Path(DATA_DIR) / 'seq-to-seq_datasets' / 'uspto_sep.tsv')
    cfg.model_path = str(Path(MODELS_DIR) / 'pre-trained' / 'combined-large' / 'step=1000000.ckpt')
    print(oc.OmegaConf.to_yaml(cfg))

    chemformer = main(args=cfg)
