from pathlib import Path


CONFIG_DIR = str(Path(__file__).resolve().parent / "config")
DATA_DIR = str(Path(__file__).resolve().parent / "bigdata")
MOLDATA_FILEPATH = str(Path(DATA_DIR) / 'seq-to-seq_datasets' / 'mol_opt.pickle') 
# ./src/molbart/bigdata/seq-to-seq_datasets/mol_opt.pickle
# ./src/molbart/bigdata/seq-to-seq_datasets/uspto_50.pickle
# ./src/molbart/bigdata/seq-to-seq_datasets/uspto_mixed.pickle
# ./src/molbart/bigdata/seq-to-seq_datasets/uspto_sep.pickle

MODELS_DIR = str(Path(__file__).resolve().parent / "bigmodels")