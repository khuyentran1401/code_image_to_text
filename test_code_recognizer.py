import pytest 
from code_recognizer import CodeCleaner
from icecream import ic

@pytest.fixture
def code_cleaner():
    code = """
    >>> class DataLoader:
    def __init__(self, data_dir: str):
    self.data_dir = data_dir
    print('Instance is created')

    def __call__(self):
    print('Instance is called')

    >>> data_loader = DataLoader('my_data_dir')
    Instance is created

    >>> data_loader( )

    Instance is called"""

    return CodeCleaner(code)

def test_replace_bad_characters():
    code = """>>> data_loader( )"""
    assert CodeCleaner.replace_bad_characters(code) ==  " data_loader()"

def test_remove_whitespace():
    code = "  hello it's me   "
    assert CodeCleaner(code).remove_whitespace() == "hello it's me"

def test_add_tab():
    code = """
    class DataLoader:
    def __init__(self, data_dir: str):
    self.data_dir = data_dir
    """

    ic(CodeCleaner().add_tab(code))

def test_detect_print_code(code_cleaner):
    print(code_cleaner.detect_print_code())

def test_clean(code_cleaner):
    code_cleaner.clean()