# Compatibility shim: old checkpoints pickled DecodeSampler under molbart.decoder
from molbart.utils.samplers.beam_search_samplers import DecodeSampler  # noqa: F401
