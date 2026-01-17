from proccessor import clean_id
def test_clean_id():
    assert clean_id("cc-75.087.345")=="75087345"
    
from proccessor import merge_name
def test_merge_name():
    assert merge_name("Jose", "Fernando")=="Jose Fernando"