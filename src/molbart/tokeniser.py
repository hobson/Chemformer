# Compatibility shim: old checkpoints pickled MolEncTokeniser from molbart.tokeniser
from molbart.utils.tokenizers import ChemformerTokenizer as MolEncTokeniser  # noqa: F401
