# seq-to-seq-datasets

`_sep` datasets contain separate reactants and reagents columns
`_mixed` datasets contain reactants and reagents both within the reactants column

The `reactants` and optional `reagents` columns separate SMILES with a `'.'` and no spaces rather than `' + '` as in more modern reaction datasets such as ORD.

The `predict.py` and `inference_score.py` scripts expect the validation dataset to be in TSV (TAB-separated values) format.

```python
>>> import pandas as pd
>>> from molbart.constants import DATA_DIR
>>> dfs = {}
... for p in 'mol_opt.pickle uspto_50.pickle uspto_mixed.pickle uspto_sep.pickle'.split():
...     df = pd.read_pickle(str(Path(DATA_DIR) / 'seq-to-seq_datasets' / p))
...     dfs[p] = df
...     print(p, df.columns)
...     # Cannot be saved to CSV because contains RDKit.Mol objects
...     # df.to_csv(str((Path(DATA_DIR) / 'seq-to-seq_datasets' / p).with_suffix('.csv')))
mol_opt.pickle Index(['property_tokens', 'input_smiles', 'input_mols', 'output_smiles',
       'output_mols', 'set'],
      dtype='object')
uspto_50.pickle Index(['reactants_mol', 'products_mol', 'reaction_type', 'set'], dtype='object')
uspto_mixed.pickle Index(['reactants_mol', 'products_mol', 'set'], dtype='object')
uspto_sep.pickle Index(['reactants_mol', 'products_mol', 'reagents_mol', 'set'], dtype='object')
```
