============================= test session starts ==============================
platform linux -- Python 3.8.20, pytest-8.3.5, pluggy-1.5.0
rootdir: /home/hobs/code/corethink/Chemformer
configfile: pyproject.toml
plugins: mock-3.14.1, hydra-core-1.3.2, datadir-1.8.0, cov-5.0.0, anyio-4.5.2
collected 81 items

tests/decoder_test.py ..FFFFFFFF                                         [ 12%]
tests/pre_train_model_test.py ......                                     [ 19%]
tests/test_atom_mapper.py .......                                        [ 28%]
tests/test_data.py ..............                                        [ 45%]
tests/test_data_utils.py ...                                             [ 49%]
tests/test_decoder.py ..........EEEEE                                    [ 67%]
tests/test_pre_train_model.py ......                                     [ 75%]
tests/test_round_trip_utils.py ..E                                       [ 79%]
tests/test_scores.py F........                                           [ 90%]
tests/test_tokenizer.py ........                                         [100%]

==================================== ERRORS ====================================
_____ ERROR at setup of test_correct_beam_size_optimized_sampler[1-beam-1] _____

round_trip_namespace_args = Namespace(backward_predictions=PosixPath('/tmp/pytest-of-hobs/pytest-1/test_correct_beam_size_optimiz0/data/example_da...ta/example_data_uspto.csv'), output_score_data='temp_metrics.csv', target_column='products', working_directory='tests')

    @pytest.fixture
    def model_batch_setup(round_trip_namespace_args):
>       config = oc.OmegaConf.load("molbart/config/round_trip_inference.yaml")

tests/conftest.py:114: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_ = 'molbart/config/round_trip_inference.yaml'

    @staticmethod
    def load(file_: Union[str, pathlib.Path, IO[Any]]) -> Union[DictConfig, ListConfig]:
        from ._utils import get_yaml_loader
    
        if isinstance(file_, (str, pathlib.Path)):
>           with io.open(os.path.abspath(file_), "r", encoding="utf-8") as f:
E           FileNotFoundError: [Errno 2] No such file or directory: '/home/hobs/code/corethink/Chemformer/molbart/config/round_trip_inference.yaml'

.venv/lib/python3.8/site-packages/omegaconf/omegaconf.py:189: FileNotFoundError
_____ ERROR at setup of test_correct_beam_size_optimized_sampler[3-beam-3] _____

round_trip_namespace_args = Namespace(backward_predictions=PosixPath('/tmp/pytest-of-hobs/pytest-1/test_correct_beam_size_optimiz1/data/example_da...ta/example_data_uspto.csv'), output_score_data='temp_metrics.csv', target_column='products', working_directory='tests')

    @pytest.fixture
    def model_batch_setup(round_trip_namespace_args):
>       config = oc.OmegaConf.load("molbart/config/round_trip_inference.yaml")

tests/conftest.py:114: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_ = 'molbart/config/round_trip_inference.yaml'

    @staticmethod
    def load(file_: Union[str, pathlib.Path, IO[Any]]) -> Union[DictConfig, ListConfig]:
        from ._utils import get_yaml_loader
    
        if isinstance(file_, (str, pathlib.Path)):
>           with io.open(os.path.abspath(file_), "r", encoding="utf-8") as f:
E           FileNotFoundError: [Errno 2] No such file or directory: '/home/hobs/code/corethink/Chemformer/molbart/config/round_trip_inference.yaml'

.venv/lib/python3.8/site-packages/omegaconf/omegaconf.py:189: FileNotFoundError
____ ERROR at setup of test_correct_beam_size_optimized_sampler[5-greedy-1] ____

round_trip_namespace_args = Namespace(backward_predictions=PosixPath('/tmp/pytest-of-hobs/pytest-1/test_correct_beam_size_optimiz2/data/example_da...ta/example_data_uspto.csv'), output_score_data='temp_metrics.csv', target_column='products', working_directory='tests')

    @pytest.fixture
    def model_batch_setup(round_trip_namespace_args):
>       config = oc.OmegaConf.load("molbart/config/round_trip_inference.yaml")

tests/conftest.py:114: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_ = 'molbart/config/round_trip_inference.yaml'

    @staticmethod
    def load(file_: Union[str, pathlib.Path, IO[Any]]) -> Union[DictConfig, ListConfig]:
        from ._utils import get_yaml_loader
    
        if isinstance(file_, (str, pathlib.Path)):
>           with io.open(os.path.abspath(file_), "r", encoding="utf-8") as f:
E           FileNotFoundError: [Errno 2] No such file or directory: '/home/hobs/code/corethink/Chemformer/molbart/config/round_trip_inference.yaml'

.venv/lib/python3.8/site-packages/omegaconf/omegaconf.py:189: FileNotFoundError
________ ERROR at setup of test_beam_search_sampler_agreement[1-greedy] ________

round_trip_namespace_args = Namespace(backward_predictions=PosixPath('/tmp/pytest-of-hobs/pytest-1/test_beam_search_sampler_agree0/data/example_da...ta/example_data_uspto.csv'), output_score_data='temp_metrics.csv', target_column='products', working_directory='tests')

    @pytest.fixture
    def model_batch_setup(round_trip_namespace_args):
>       config = oc.OmegaConf.load("molbart/config/round_trip_inference.yaml")

tests/conftest.py:114: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_ = 'molbart/config/round_trip_inference.yaml'

    @staticmethod
    def load(file_: Union[str, pathlib.Path, IO[Any]]) -> Union[DictConfig, ListConfig]:
        from ._utils import get_yaml_loader
    
        if isinstance(file_, (str, pathlib.Path)):
>           with io.open(os.path.abspath(file_), "r", encoding="utf-8") as f:
E           FileNotFoundError: [Errno 2] No such file or directory: '/home/hobs/code/corethink/Chemformer/molbart/config/round_trip_inference.yaml'

.venv/lib/python3.8/site-packages/omegaconf/omegaconf.py:189: FileNotFoundError
_________ ERROR at setup of test_beam_search_sampler_agreement[2-beam] _________

round_trip_namespace_args = Namespace(backward_predictions=PosixPath('/tmp/pytest-of-hobs/pytest-1/test_beam_search_sampler_agree1/data/example_da...ta/example_data_uspto.csv'), output_score_data='temp_metrics.csv', target_column='products', working_directory='tests')

    @pytest.fixture
    def model_batch_setup(round_trip_namespace_args):
>       config = oc.OmegaConf.load("molbart/config/round_trip_inference.yaml")

tests/conftest.py:114: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_ = 'molbart/config/round_trip_inference.yaml'

    @staticmethod
    def load(file_: Union[str, pathlib.Path, IO[Any]]) -> Union[DictConfig, ListConfig]:
        from ._utils import get_yaml_loader
    
        if isinstance(file_, (str, pathlib.Path)):
>           with io.open(os.path.abspath(file_), "r", encoding="utf-8") as f:
E           FileNotFoundError: [Errno 2] No such file or directory: '/home/hobs/code/corethink/Chemformer/molbart/config/round_trip_inference.yaml'

.venv/lib/python3.8/site-packages/omegaconf/omegaconf.py:189: FileNotFoundError
______________ ERROR at setup of test_compute_round_trip_accuracy ______________

round_trip_namespace_args = Namespace(backward_predictions=PosixPath('/tmp/pytest-of-hobs/pytest-1/test_compute_round_trip_accura0/data/example_da...ta/example_data_uspto.csv'), output_score_data='temp_metrics.csv', target_column='products', working_directory='tests')

    @pytest.fixture
    def model_batch_setup(round_trip_namespace_args):
>       config = oc.OmegaConf.load("molbart/config/round_trip_inference.yaml")

tests/conftest.py:114: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_ = 'molbart/config/round_trip_inference.yaml'

    @staticmethod
    def load(file_: Union[str, pathlib.Path, IO[Any]]) -> Union[DictConfig, ListConfig]:
        from ._utils import get_yaml_loader
    
        if isinstance(file_, (str, pathlib.Path)):
>           with io.open(os.path.abspath(file_), "r", encoding="utf-8") as f:
E           FileNotFoundError: [Errno 2] No such file or directory: '/home/hobs/code/corethink/Chemformer/molbart/config/round_trip_inference.yaml'

.venv/lib/python3.8/site-packages/omegaconf/omegaconf.py:189: FileNotFoundError
=================================== FAILURES ===================================
___________________________ test_greedy_calls_decode ___________________________

thing = <module 'molbart' from '/home/hobs/code/corethink/Chemformer/src/molbart/__init__.py'>
comp = 'modules', import_path = 'molbart.modules'

    def _dot_lookup(thing, comp, import_path):
        try:
>           return getattr(thing, comp)
E           AttributeError: module 'molbart' has no attribute 'modules'

../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1215: AttributeError

During handling of the above exception, another exception occurred:

mocker = <pytest_mock.plugin.MockerFixture object at 0x7342b2bf4c40>

    def test_greedy_calls_decode(mocker):
>       mocked_tokenizer = mocker.patch("molbart.modules.tokenizer.ChemformerTokenizer")

tests/decoder_test.py:30: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:439: in __call__
    return self._start_patch(
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:257: in _start_patch
    mocked: MockType = p.start()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1529: in start
    result = self.__enter__()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1377: in __enter__
    self.target = self.getter()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1552: in <lambda>
    getter = lambda: _importer(target)
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1228: in _importer
    thing = _dot_lookup(thing, comp, import_path)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

thing = <module 'molbart' from '/home/hobs/code/corethink/Chemformer/src/molbart/__init__.py'>
comp = 'modules', import_path = 'molbart.modules'

    def _dot_lookup(thing, comp, import_path):
        try:
            return getattr(thing, comp)
        except AttributeError:
>           __import__(import_path)
E           ModuleNotFoundError: No module named 'molbart.modules'

../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1217: ModuleNotFoundError
___________________________ test_greedy_chooses_max ____________________________

thing = <module 'molbart' from '/home/hobs/code/corethink/Chemformer/src/molbart/__init__.py'>
comp = 'modules', import_path = 'molbart.modules'

    def _dot_lookup(thing, comp, import_path):
        try:
>           return getattr(thing, comp)
E           AttributeError: module 'molbart' has no attribute 'modules'

../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1215: AttributeError

During handling of the above exception, another exception occurred:

mocker = <pytest_mock.plugin.MockerFixture object at 0x7342b2a2fd00>

    def test_greedy_chooses_max(mocker):
>       mocked_tokenizer = mocker.patch("molbart.modules.tokenizer.ChemformerTokenizer")

tests/decoder_test.py:53: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:439: in __call__
    return self._start_patch(
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:257: in _start_patch
    mocked: MockType = p.start()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1529: in start
    result = self.__enter__()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1377: in __enter__
    self.target = self.getter()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1552: in <lambda>
    getter = lambda: _importer(target)
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1228: in _importer
    thing = _dot_lookup(thing, comp, import_path)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

thing = <module 'molbart' from '/home/hobs/code/corethink/Chemformer/src/molbart/__init__.py'>
comp = 'modules', import_path = 'molbart.modules'

    def _dot_lookup(thing, comp, import_path):
        try:
            return getattr(thing, comp)
        except AttributeError:
>           __import__(import_path)
E           ModuleNotFoundError: No module named 'molbart.modules'

../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1217: ModuleNotFoundError
________________________ test_greedy_stops_at_end_token ________________________

thing = <module 'molbart' from '/home/hobs/code/corethink/Chemformer/src/molbart/__init__.py'>
comp = 'modules', import_path = 'molbart.modules'

    def _dot_lookup(thing, comp, import_path):
        try:
>           return getattr(thing, comp)
E           AttributeError: module 'molbart' has no attribute 'modules'

../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1215: AttributeError

During handling of the above exception, another exception occurred:

mocker = <pytest_mock.plugin.MockerFixture object at 0x7342b29f9580>

    def test_greedy_stops_at_end_token(mocker):
>       mocked_tokenizer = mocker.patch("molbart.modules.tokenizer.ChemformerTokenizer")

tests/decoder_test.py:82: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:439: in __call__
    return self._start_patch(
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:257: in _start_patch
    mocked: MockType = p.start()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1529: in start
    result = self.__enter__()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1377: in __enter__
    self.target = self.getter()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1552: in <lambda>
    getter = lambda: _importer(target)
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1228: in _importer
    thing = _dot_lookup(thing, comp, import_path)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

thing = <module 'molbart' from '/home/hobs/code/corethink/Chemformer/src/molbart/__init__.py'>
comp = 'modules', import_path = 'molbart.modules'

    def _dot_lookup(thing, comp, import_path):
        try:
            return getattr(thing, comp)
        except AttributeError:
>           __import__(import_path)
E           ModuleNotFoundError: No module named 'molbart.modules'

../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1217: ModuleNotFoundError
_______________________________ test_greedy_lls ________________________________

thing = <module 'molbart' from '/home/hobs/code/corethink/Chemformer/src/molbart/__init__.py'>
comp = 'modules', import_path = 'molbart.modules'

    def _dot_lookup(thing, comp, import_path):
        try:
>           return getattr(thing, comp)
E           AttributeError: module 'molbart' has no attribute 'modules'

../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1215: AttributeError

During handling of the above exception, another exception occurred:

mocker = <pytest_mock.plugin.MockerFixture object at 0x7342b24b0df0>

    def test_greedy_lls(mocker):
>       mocked_tokenizer = mocker.patch("molbart.modules.tokenizer.ChemformerTokenizer")

tests/decoder_test.py:112: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:439: in __call__
    return self._start_patch(
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:257: in _start_patch
    mocked: MockType = p.start()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1529: in start
    result = self.__enter__()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1377: in __enter__
    self.target = self.getter()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1552: in <lambda>
    getter = lambda: _importer(target)
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1228: in _importer
    thing = _dot_lookup(thing, comp, import_path)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

thing = <module 'molbart' from '/home/hobs/code/corethink/Chemformer/src/molbart/__init__.py'>
comp = 'modules', import_path = 'molbart.modules'

    def _dot_lookup(thing, comp, import_path):
        try:
            return getattr(thing, comp)
        except AttributeError:
>           __import__(import_path)
E           ModuleNotFoundError: No module named 'molbart.modules'

../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1217: ModuleNotFoundError
____________________________ test_beam_calls_decode ____________________________

thing = <module 'molbart' from '/home/hobs/code/corethink/Chemformer/src/molbart/__init__.py'>
comp = 'modules', import_path = 'molbart.modules'

    def _dot_lookup(thing, comp, import_path):
        try:
>           return getattr(thing, comp)
E           AttributeError: module 'molbart' has no attribute 'modules'

../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1215: AttributeError

During handling of the above exception, another exception occurred:

mocker = <pytest_mock.plugin.MockerFixture object at 0x7342b29aa640>

    def test_beam_calls_decode(mocker):
>       mocked_tokenizer = mocker.patch("molbart.modules.tokenizer.ChemformerTokenizer")

tests/decoder_test.py:142: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:439: in __call__
    return self._start_patch(
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:257: in _start_patch
    mocked: MockType = p.start()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1529: in start
    result = self.__enter__()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1377: in __enter__
    self.target = self.getter()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1552: in <lambda>
    getter = lambda: _importer(target)
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1228: in _importer
    thing = _dot_lookup(thing, comp, import_path)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

thing = <module 'molbart' from '/home/hobs/code/corethink/Chemformer/src/molbart/__init__.py'>
comp = 'modules', import_path = 'molbart.modules'

    def _dot_lookup(thing, comp, import_path):
        try:
            return getattr(thing, comp)
        except AttributeError:
>           __import__(import_path)
E           ModuleNotFoundError: No module named 'molbart.modules'

../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1217: ModuleNotFoundError
_______________________ test_beam_chooses_correct_tokens _______________________

thing = <module 'molbart' from '/home/hobs/code/corethink/Chemformer/src/molbart/__init__.py'>
comp = 'modules', import_path = 'molbart.modules'

    def _dot_lookup(thing, comp, import_path):
        try:
>           return getattr(thing, comp)
E           AttributeError: module 'molbart' has no attribute 'modules'

../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1215: AttributeError

During handling of the above exception, another exception occurred:

mocker = <pytest_mock.plugin.MockerFixture object at 0x7342b24a7e50>

    def test_beam_chooses_correct_tokens(mocker):
>       mocked_tokenizer = mocker.patch("molbart.modules.tokenizer.ChemformerTokenizer")

tests/decoder_test.py:165: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:439: in __call__
    return self._start_patch(
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:257: in _start_patch
    mocked: MockType = p.start()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1529: in start
    result = self.__enter__()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1377: in __enter__
    self.target = self.getter()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1552: in <lambda>
    getter = lambda: _importer(target)
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1228: in _importer
    thing = _dot_lookup(thing, comp, import_path)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

thing = <module 'molbart' from '/home/hobs/code/corethink/Chemformer/src/molbart/__init__.py'>
comp = 'modules', import_path = 'molbart.modules'

    def _dot_lookup(thing, comp, import_path):
        try:
            return getattr(thing, comp)
        except AttributeError:
>           __import__(import_path)
E           ModuleNotFoundError: No module named 'molbart.modules'

../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1217: ModuleNotFoundError
_________________________ test_beam_stops_at_end_token _________________________

thing = <module 'molbart' from '/home/hobs/code/corethink/Chemformer/src/molbart/__init__.py'>
comp = 'modules', import_path = 'molbart.modules'

    def _dot_lookup(thing, comp, import_path):
        try:
>           return getattr(thing, comp)
E           AttributeError: module 'molbart' has no attribute 'modules'

../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1215: AttributeError

During handling of the above exception, another exception occurred:

mocker = <pytest_mock.plugin.MockerFixture object at 0x7342b2947550>

    def test_beam_stops_at_end_token(mocker):
>       mocked_tokenizer = mocker.patch("molbart.modules.tokenizer.ChemformerTokenizer")

tests/decoder_test.py:212: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:439: in __call__
    return self._start_patch(
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:257: in _start_patch
    mocked: MockType = p.start()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1529: in start
    result = self.__enter__()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1377: in __enter__
    self.target = self.getter()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1552: in <lambda>
    getter = lambda: _importer(target)
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1228: in _importer
    thing = _dot_lookup(thing, comp, import_path)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

thing = <module 'molbart' from '/home/hobs/code/corethink/Chemformer/src/molbart/__init__.py'>
comp = 'modules', import_path = 'molbart.modules'

    def _dot_lookup(thing, comp, import_path):
        try:
            return getattr(thing, comp)
        except AttributeError:
>           __import__(import_path)
E           ModuleNotFoundError: No module named 'molbart.modules'

../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1217: ModuleNotFoundError
________________________________ test_beam_lls _________________________________

thing = <module 'molbart' from '/home/hobs/code/corethink/Chemformer/src/molbart/__init__.py'>
comp = 'modules', import_path = 'molbart.modules'

    def _dot_lookup(thing, comp, import_path):
        try:
>           return getattr(thing, comp)
E           AttributeError: module 'molbart' has no attribute 'modules'

../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1215: AttributeError

During handling of the above exception, another exception occurred:

mocker = <pytest_mock.plugin.MockerFixture object at 0x7342b2486b50>

    def test_beam_lls(mocker):
>       mocked_tokenizer = mocker.patch("molbart.modules.tokenizer.ChemformerTokenizer")

tests/decoder_test.py:259: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:439: in __call__
    return self._start_patch(
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:257: in _start_patch
    mocked: MockType = p.start()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1529: in start
    result = self.__enter__()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1377: in __enter__
    self.target = self.getter()
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1552: in <lambda>
    getter = lambda: _importer(target)
../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1228: in _importer
    thing = _dot_lookup(thing, comp, import_path)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

thing = <module 'molbart' from '/home/hobs/code/corethink/Chemformer/src/molbart/__init__.py'>
comp = 'modules', import_path = 'molbart.modules'

    def _dot_lookup(thing, comp, import_path):
        try:
            return getattr(thing, comp)
        except AttributeError:
>           __import__(import_path)
E           ModuleNotFoundError: No module named 'molbart.modules'

../../../.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/unittest/mock.py:1217: ModuleNotFoundError
________________________ test_default_inference_scoring ________________________

    def test_default_inference_scoring():
>       config = oc.OmegaConf.load("molbart/config/inference_score.yaml")

tests/test_scores.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_ = 'molbart/config/inference_score.yaml'

    @staticmethod
    def load(file_: Union[str, pathlib.Path, IO[Any]]) -> Union[DictConfig, ListConfig]:
        from ._utils import get_yaml_loader
    
        if isinstance(file_, (str, pathlib.Path)):
>           with io.open(os.path.abspath(file_), "r", encoding="utf-8") as f:
E           FileNotFoundError: [Errno 2] No such file or directory: '/home/hobs/code/corethink/Chemformer/molbart/config/inference_score.yaml'

.venv/lib/python3.8/site-packages/omegaconf/omegaconf.py:189: FileNotFoundError
=============================== warnings summary ===============================
.venv/lib/python3.8/site-packages/pytorch_lightning/utilities/imports.py:21
  /home/hobs/code/corethink/Chemformer/.venv/lib/python3.8/site-packages/pytorch_lightning/utilities/imports.py:21: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    from pkg_resources import DistributionNotFound, get_distribution

.venv/lib/python3.8/site-packages/pytorch_lightning/utilities/imports.py:45
.venv/lib/python3.8/site-packages/pytorch_lightning/utilities/imports.py:45
.venv/lib/python3.8/site-packages/pytorch_lightning/utilities/imports.py:45
  /home/hobs/code/corethink/Chemformer/.venv/lib/python3.8/site-packages/pytorch_lightning/utilities/imports.py:45: DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.
    pkg_version = LooseVersion(get_distribution(package).version)

.venv/lib/python3.8/site-packages/pytorch_lightning/utilities/imports.py:46
.venv/lib/python3.8/site-packages/pytorch_lightning/utilities/imports.py:46
.venv/lib/python3.8/site-packages/pytorch_lightning/utilities/imports.py:46
  /home/hobs/code/corethink/Chemformer/.venv/lib/python3.8/site-packages/pytorch_lightning/utilities/imports.py:46: DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.
    return op(pkg_version, LooseVersion(version))

.venv/lib/python3.8/site-packages/torch/utils/tensorboard/__init__.py:3
.venv/lib/python3.8/site-packages/torch/utils/tensorboard/__init__.py:3
  /home/hobs/code/corethink/Chemformer/.venv/lib/python3.8/site-packages/torch/utils/tensorboard/__init__.py:3: DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.
    if not hasattr(tensorboard, '__version__') or LooseVersion(tensorboard.__version__) < LooseVersion('1.15'):

.venv/lib/python3.8/site-packages/pytorch_lightning/__init__.py:78
  /home/hobs/code/corethink/Chemformer/.venv/lib/python3.8/site-packages/pytorch_lightning/__init__.py:78: DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('pytorch_lightning')`.
  Implementing implicit namespace packages (as specified in PEP 420) is preferred to `pkg_resources.declare_namespace`. See https://setuptools.pypa.io/en/latest/references/keywords.html#keyword-namespace-packages
    __import__('pkg_resources').declare_namespace(__name__)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED tests/decoder_test.py::test_greedy_calls_decode - ModuleNotFoundError:...
FAILED tests/decoder_test.py::test_greedy_chooses_max - ModuleNotFoundError: ...
FAILED tests/decoder_test.py::test_greedy_stops_at_end_token - ModuleNotFound...
FAILED tests/decoder_test.py::test_greedy_lls - ModuleNotFoundError: No modul...
FAILED tests/decoder_test.py::test_beam_calls_decode - ModuleNotFoundError: N...
FAILED tests/decoder_test.py::test_beam_chooses_correct_tokens - ModuleNotFou...
FAILED tests/decoder_test.py::test_beam_stops_at_end_token - ModuleNotFoundEr...
FAILED tests/decoder_test.py::test_beam_lls - ModuleNotFoundError: No module ...
FAILED tests/test_scores.py::test_default_inference_scoring - FileNotFoundErr...
ERROR tests/test_decoder.py::test_correct_beam_size_optimized_sampler[1-beam-1]
ERROR tests/test_decoder.py::test_correct_beam_size_optimized_sampler[3-beam-3]
ERROR tests/test_decoder.py::test_correct_beam_size_optimized_sampler[5-greedy-1]
ERROR tests/test_decoder.py::test_beam_search_sampler_agreement[1-greedy] - F...
ERROR tests/test_decoder.py::test_beam_search_sampler_agreement[2-beam] - Fil...
ERROR tests/test_round_trip_utils.py::test_compute_round_trip_accuracy - File...
============= 9 failed, 66 passed, 10 warnings, 6 errors in 1.97s ==============
