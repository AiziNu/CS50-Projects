from twttr import convert_twttr


def main():
    test_twttr()

def test_twttr():
    assert convert_twttr("TOMORROW") == "tmttw"
    assert convert_twttr("TWitter") == "twttr"
    assert convert_twttr("hello") == "hll"
    assert convert_twttr("12345") == "12345"
    assert convert_twttr("Symbol$%^") == "smbl$%^"
    assert


