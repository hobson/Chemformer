# Dependencies iPython, numpy, Jupyter

If you install iPython or Jupyter in python~=3.10, it will break molbart which depends on numpy < 2.

Added it as a direct dependency in python 3.8 and it worked find.

## `ipython`

```python
>>> from molbart import predict

A module that was compiled using NumPy 1.x cannot be run in
NumPy 2.0.2 as it may crash. To support both 1.x and 2.x
versions of NumPy, modules must be compiled with NumPy 2.0.
Some module may need to rebuild instead e.g. with 'pybind11>=2.12'.

If you are a user of the module, the easiest solution will be to
downgrade to 'numpy<2' or try to upgrade the affected module.
We expect that some modules will need time to support NumPy 2.

Traceback (most recent call last):  File "/home/hobs/code/corethink/Chemformer/.venv/bin/ipython", line 10, in <module>
    sys.exit(start_ipython())
  File "/home/hobs/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/IPython/__init__.py", line 129, in start_ipython
    return launch_new_instance(argv=argv, **kwargs)
  File "/home/hobs/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/traitlets/config/application.py", line 1075, in launch_instance
    app.start()
  File "/home/hobs/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/IPython/terminal/ipapp.py", line 317, in start
    self.shell.mainloop()
  File "/home/hobs/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/IPython/terminal/interactiveshell.py", line 887, in mainloop
    self.interact()
  File "/home/hobs/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/IPython/terminal/interactiveshell.py", line 880, in interact
    self.run_cell(code, store_history=True)
  File "/home/hobs/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/IPython/core/interactiveshell.py", line 3048, in run_cell
    result = self._run_cell(
  File "/home/hobs/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/IPython/core/interactiveshell.py", line 3103, in _run_cell
    result = runner(coro)
  File "/home/hobs/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/IPython/core/async_helpers.py", line 129, in _pseudo_sync_runner
    coro.send(None)
  File "/home/hobs/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/IPython/core/interactiveshell.py", line 3308, in run_cell_async
    has_raised = await self.run_ast_nodes(code_ast.body, cell_name,
  File "/home/hobs/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/IPython/core/interactiveshell.py", line 3490, in run_ast_nodes
    if await self.run_code(code, result, async_=asy):
  File "/home/hobs/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/IPython/core/interactiveshell.py", line 3550, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-1-4c313c916154>", line 1, in <module>
    from molbart import predict
  File "/home/hobs/code/corethink/Chemformer/src/molbart/predict.py", line 4, in <module>
    import molbart.utils.data_utils as util
  File "/home/hobs/code/corethink/Chemformer/src/molbart/utils/data_utils.py", line 6, in <module>
    import pytorch_lightning as pl
  File "/home/hobs/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/pytorch_lightning/__init__.py", line 62, in <module>
    from pytorch_lightning import metrics
  File "/home/hobs/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/pytorch_lightning/metrics/__init__.py", line 14, in <module>
    from pytorch_lightning.metrics.classification import (  # noqa: F401
  File "/home/hobs/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/pytorch_lightning/metrics/classification/__init__.py", line 14, in <module>
    from pytorch_lightning.metrics.classification.accuracy import Accuracy  # noqa: F401
  File "/home/hobs/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/pytorch_lightning/metrics/classification/accuracy.py", line 16, in <module>
    import torch
  File "/home/hobs/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/torch/__init__.py", line 196, in <module>
    from torch._C import *
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[1], line 1
----> 1 from molbart import predict

File ~/code/corethink/Chemformer/src/molbart/predict.py:4
      1 import hydra
      2 import pandas as pd
----> 4 import molbart.utils.data_utils as util
      5 from molbart.models import Chemformer
      8 def write_predictions(args, smiles, log_lhs, original_smiles):

File ~/code/corethink/Chemformer/src/molbart/utils/data_utils.py:6
      4 import numpy as np
      5 import pandas as pd
----> 6 import pytorch_lightning as pl
      7 import torch
      9 from molbart.models.transformer_models import BARTModel, UnifiedModel

File ~/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/pytorch_lightning/__init__.py:62
     59     sys.stdout.write(f'Partial import of `{__name__}` during the build process.\n')  # pragma: no-cover
     60     # We are not importing the rest of the lightning during the build process, as it may not be compiled yet
     61 else:
---> 62     from pytorch_lightning import metrics
     63     from pytorch_lightning.callbacks import Callback
     64     from pytorch_lightning.core import LightningDataModule, LightningModule

File ~/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/pytorch_lightning/metrics/__init__.py:14
      1 # Copyright The PyTorch Lightning team.
      2 #
      3 # Licensed under the Apache License, Version 2.0 (the "License");
   (...)
     12 # See the License for the specific language governing permissions and
     13 # limitations under the License.
---> 14 from pytorch_lightning.metrics.classification import (  # noqa: F401
     15     Accuracy,
     16     AUC,
     17     AUROC,
     18     AveragePrecision,
     19     ConfusionMatrix,
     20     F1,
     21     FBeta,
     22     HammingDistance,
     23     IoU,
     24     Precision,
     25     PrecisionRecallCurve,
     26     Recall,
     27     ROC,
     28     StatScores,
     29 )
     30 from pytorch_lightning.metrics.metric import Metric, MetricCollection  # noqa: F401
     31 from pytorch_lightning.metrics.regression import (  # noqa: F401
     32     ExplainedVariance,
     33     MeanAbsoluteError,
   (...)
     38     SSIM,
     39 )

File ~/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/pytorch_lightning/metrics/classification/__init__.py:14
      1 # Copyright The PyTorch Lightning team.
      2 #
      3 # Licensed under the Apache License, Version 2.0 (the "License");
   (...)
     12 # See the License for the specific language governing permissions and
     13 # limitations under the License.
---> 14 from pytorch_lightning.metrics.classification.accuracy import Accuracy  # noqa: F401
     15 from pytorch_lightning.metrics.classification.auc import AUC  # noqa: F401
     16 from pytorch_lightning.metrics.classification.auroc import AUROC  # noqa: F401

File ~/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/pytorch_lightning/metrics/classification/accuracy.py:16
      1 # Copyright The PyTorch Lightning team.
      2 #
      3 # Licensed under the Apache License, Version 2.0 (the "License");
   (...)
     12 # See the License for the specific language governing permissions and
     13 # limitations under the License.
     14 from typing import Any, Callable, Optional
---> 16 import torch
     18 from pytorch_lightning.metrics.functional.accuracy import _accuracy_compute, _accuracy_update
     19 from pytorch_lightning.metrics.metric import Metric

File ~/code/corethink/Chemformer/.venv/lib/python3.9/site-packages/torch/__init__.py:196
    194     if USE_GLOBAL_DEPS:
    195         _load_global_deps()
--> 196     from torch._C import *
    198 # Appease the type checker; ordinarily this binding is inserted by the
    199 # torch._C module initialization code in C
    200 if TYPE_CHECKING:

AttributeError: _ARRAY_API not found
```
