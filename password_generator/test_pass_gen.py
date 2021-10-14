from pass_gen import GenPass

def test_constructor():
    p = GenPass()
    assert isinstance(p, GenPass)
    assert p.passwd(char_set=12, pass_len=7) == "xxxxxxx"