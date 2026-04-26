from pathlib import Path
import os
import dotenv

ENV = dict(
    DEBUG = True,
    PG_USERNAME = 'hobs',
    PG_PASSWORD = '',
    PG_HOST = 'localhost',
    PG_PORT = 5432,
    PG_DATABASE = 'pubchem',
    ZYDUS_PORT = 8081,
)

# Using `dotenv_values` instead of `load_dotenv` creates precedence order: 
#  1. .env overrides defaults in constants.ENV above
#  2. OS.environ to overrides both defaults in `ENV` var above and .env file
ENV.update(dotenv.dotenv_values())
ENV.update(dict(os.environ))
for k in ENV:
    locals()[k] = ENV[k]

CONFIG_DIR = str(Path(__file__).resolve().parent / "config")
DATA_DIR = str(Path(__file__).resolve().parent / "bigdata")
MOLDATA_FILEPATH = str(Path(DATA_DIR) / 'seq-to-seq_datasets' / 'mol_opt.pickle') 
# ./src/molbart/bigdata/seq-to-seq_datasets/mol_opt.pickle
# ./src/molbart/bigdata/seq-to-seq_datasets/uspto_50.pickle
# ./src/molbart/bigdata/seq-to-seq_datasets/uspto_mixed.pickle
# ./src/molbart/bigdata/seq-to-seq_datasets/uspto_sep.pickle

MODELS_DIR = str(Path(__file__).resolve().parent / "bigmodels")