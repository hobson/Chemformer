# Chemformer Retrosynthesis Model Evaluation Report

**Model:** Chemformer BART (backward prediction, USPTO-50K fine-tune)
**Checkpoint:** `backward_uspto50k.ckpt` ([Figshare 42009888](https://figshare.com/articles/dataset/Chemformer/14766561))
**Service:** `https://chemformer-retrosynthesis-knq67derjq-uc.a.run.app`
**Date:** 2026-05-08

---

## Summary

| Molecule | MW (Da) | Top-1 log-likelihood | Top-1 valid? | Chemically correct? |
|---|---|---|---|---|
| Aspirin | 180 | −0.74 | Yes | Yes |
| Ibuprofen | 206 | −0.96 | Yes | Yes |
| Orforglipron | 881 | −24.1 | Partial | No |

The model performs well on small, drug-like molecules within the training distribution (simple organic reactions, MW < 500 Da). It fails gracefully on Orforglipron, a structurally complex modern GLP-1 receptor agonist far outside the training chemical space.

---

## Test Setup

The service accepts a POST request with a product SMILES and returns beam-search retrosynthesis predictions ranked by log-likelihood.

```python
import requests

SERVICE_URL = "https://chemformer-retrosynthesis-knq67derjq-uc.a.run.app"

def predict_retrosynthesis(smiles: str, n_beams: int = 5) -> dict:
    response = requests.post(
        f"{SERVICE_URL}/retrosynthesis/predict",
        json={"smiles": smiles, "n_beams": n_beams},
        timeout=180,
    )
    response.raise_for_status()
    return response.json()
```

---

## Aspirin

**SMILES:** `CC(=O)Oc1ccccc1C(=O)O`
**MW:** 180.16 Da — simple aromatic ester

```python
result = predict_retrosynthesis("CC(=O)Oc1ccccc1C(=O)O", n_beams=5)
for i, p in enumerate(result["predictions"], 1):
    print(f"Beam {i} (ll={p['log_likelihood']:.3f}): {p['reactants_smiles']}")
```

**Output:**
```
Beam 1 (ll=-0.742): CC(=O)Cl.O=C(O)c1ccccc1O
Beam 2 (ll=-6.260): c1ccc(O)c(C(O)=O)c1.ClC(=O)C
Beam 3 (ll=-6.308): c1ccc(O)c(C(=O)O)c1.ClC(=O)C
Beam 4 (ll=-6.372): c1ccc(O)c(C(O)=O)c1.ClC(C)=O
Beam 5 (ll=-6.421): c1ccc(O)c(C(=O)O)c1.ClC(C)=O
```

**Assessment:** Excellent. Beam 1 correctly identifies the classic acetylation route:
- **Reactant 1:** `CC(=O)Cl` — acetyl chloride
- **Reactant 2:** `O=C(O)c1ccccc1O` — salicylic acid

This is the exact industrially used synthesis. Beams 2–5 are canonically equivalent representations of the same two reactants. The high confidence (log-likelihood −0.74) reflects that this reaction class appears frequently in USPTO-50K.

---

## Ibuprofen

**SMILES:** `CC(C)Cc1ccc(cc1)C(C)C(=O)O`
**MW:** 206.28 Da — substituted arylpropionic acid

```python
result = predict_retrosynthesis("CC(C)Cc1ccc(cc1)C(C)C(=O)O", n_beams=5)
for i, p in enumerate(result["predictions"], 1):
    print(f"Beam {i} (ll={p['log_likelihood']:.3f}): {p['reactants_smiles']}")
```

**Output:**
```
Beam 1 (ll=-0.964): CCOC(=O)C(C)c1ccc(CC(C)C)cc1
Beam 2 (ll=-2.301): CC(C)Cc1ccc(C(C)C(=O)OCC)cc1
Beam 3 (ll=-4.142): c1cc(CC(C)C)ccc1C(C)C(=O)OCC
Beam 4 (ll=-4.144): c1cc(CC(C)C)ccc1C(C)C(OCC)=O
Beam 5 (ll=-4.225): c1c(CC(C)C)ccc(C(C)C(=O)OCC)c1
```

**Assessment:** Good. All five beams predict ester hydrolysis (ethyl ester → carboxylic acid), identifying `CCOC(=O)C(C)c1ccc(CC(C)C)cc1` (ethyl ibuprofen ester) as the precursor. This is a valid retrosynthetic disconnection — ester hydrolysis is a standard deprotection step in ibuprofen synthesis routes. The slight confidence drop vs aspirin (−0.96 vs −0.74) likely reflects the additional alkyl substitution complexity. Beams 2–5 are equivalent SMILES representations with minor reordering.

Note: the industrial Boot–Nicholson synthesis of ibuprofen uses a different route (Friedel-Crafts acylation of isobutylbenzene), which is not predicted here. The model correctly identifies a valid route but not necessarily the most industrially common one.

---

## Orforglipron

**SMILES:** `C[C@H]1C[C@]1(C2=NOC(=O)N2)N3C4=C(C=C(C=C4)[C@H]5CCOC(C5)(C)C)C=C3C(=O)N6CCC7=NN(C(=C7[C@@H]6C)N8C=CN(C8=O)C9=C(C1=C(C=C9)N(N=C1)C)F)C1=CC(=C(C(=C1)C)F)C`
**MW:** 881 Da — oral GLP-1 receptor agonist (Eli Lilly, 2024)

```python
orforglipron_smiles = (
    "C[C@H]1C[C@]1(C2=NOC(=O)N2)"
    "N3C4=C(C=C(C=C4)[C@H]5CCOC(C5)(C)C)C=C3"
    "C(=O)N6CCC7=NN(C(=C7[C@@H]6C)"
    "N8C=CN(C8=O)C9=C(C1=C(C=C9)N(N=C1)C)F)"
    "C1=CC(=C(C(=C1)C)F)C"
)
result = predict_retrosynthesis(orforglipron_smiles, n_beams=5)
for i, p in enumerate(result["predictions"], 1):
    print(f"Beam {i} (ll={p['log_likelihood']:.3f}): {p['reactants_smiles'][:80]}...")
```

**Output:**
```
Beam 1 (ll=-24.058): C=CC1=C(C2=NOC(=O)N2)N2C(=O)C3=CC4=CC(C=C(C)C)[C@H]5CCOC(C)(C)C5=CN4C(=O)...
Beam 2 (ll=-24.109): C=CC1=C(C2=NOC(=O)N2)N2C(=O)C3=CC4=CC(C=C(C)C)[C@H]5CCOC(C)(C)C5=CN4C(=O)...
Beam 3 (ll=-24.753): C=CC1=C(C2=NOC(=O)N2)N2C(=O)C3=CC4=CC(C=C(C)C)[C@H]5CCOC(C)(C)C5=CN4C(=O)...
Beam 4 (ll=-25.542): ...C(=O)N3C[C@@H]2C1.NC(=O)O
Beam 5 (ll=-25.654): C=CC1=C(C2=NOC(=O)N2)N2C(=O)C3=CC4=CC(C=C(C)C)[C@H]5CCOC(C)(C)C5=CN4C(=O)...
```

**Assessment:** Poor, as expected. Several failure modes are evident:

1. **Very low confidence** — log-likelihoods of −24 to −26, compared to −0.7 to −1.0 for simple drugs. The model assigns near-zero probability to any single-step route.
2. **No clean disconnections** — predicted reactants are large, complex molecules nearly as difficult to synthesize as the product itself. No meaningful bonds are being broken.
3. **Out-of-distribution molecule** — Orforglipron contains structural motifs uncommon in USPTO-50K: a cyclopropyl-urea warhead, a triazolopyrimidine-piperidinyl core, multiple difluorophenyl groups, and five stereocenters. The training set is dominated by 2–4 step reactions on molecules with MW < 500 Da.

---

## Conclusions

### What works well
- Small molecules (MW < 300 Da) within common synthetic chemistry classes
- High-confidence predictions (log-likelihood > −2) correlate with correct and well-known routes
- Multiple beams often represent the same correct route with canonical SMILES variants, indicating high model certainty

### Limitations
- **Training distribution cutoff:** USPTO-50K covers reactions up to ~2016 and skews toward simple academic organic chemistry. Modern drug candidates like Orforglipron fall outside this distribution.
- **Single-step only:** The service predicts one retrosynthetic step. Complex targets require chained multi-step planning (AiZynthFinder, ASKCOS, IBM RXN).
- **No stereochemistry reasoning:** The model does not reason about whether the predicted route will reproduce the correct stereochemistry.
- **SMILES canonicalization:** Top beams are often SMILES-equivalent representations of the same reactants rather than genuinely diverse routes.

### Recommended use cases
- Quick single-step retrosynthetic lookup for lead optimization analogs
- Reaction class classification (ester hydrolysis, acylation, etc.)
- Filtering/ranking candidate routes generated by other tools

### Not recommended for
- Novel drug candidates outside USPTO-50K chemistry space (MW > 500 Da, modern heterocyclic scaffolds)
- Stereoselective synthesis planning
- Final synthetic route selection without expert chemist review
