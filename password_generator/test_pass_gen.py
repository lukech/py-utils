from pass_gen import GenPass
import pytest

@pytest.fixture
def gen_pass():
    return GenPass()

def test_constructor():
    p = GenPass()
    assert isinstance(p, GenPass)

def test_pass_len(gen_pass):
    # Default value
    assert gen_pass.pass_len == 8

    gen_pass.pass_len = 12
    assert gen_pass.pass_len == 12 

def test_char_set(gen_pass):
    # Default value
    assert gen_pass.char_set == \
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"
 
    gen_pass.char_set = "abcd01@"
    assert gen_pass.char_set == "abcd01@"