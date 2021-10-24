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


def test_passwd_len(gen_pass):
    # Default values
    assert len(gen_pass.passwd()) == 8

    # Set password length
    assert len(gen_pass.passwd(pass_len=10)) == 10

    # Set password character set
    assert len(gen_pass.passwd(char_set="abcdefgh0123@#")) == 10

    # Set both password length and character set
    assert len(gen_pass.passwd(pass_len=12, char_set="abcdefgh0123@#")) == 12
