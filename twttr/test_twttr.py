from twttr import convert_twttr


def main():
    test_twttr()

def test_twttr():
    assert convert_twttr("TOMORROW") == "TMRRW"
    assert convert_twttr("TWitter") == "TWttr"
    assert convert_twttr("hello") == "hll"
    assert convert_twttr("12345") == "12345"
    assert convert_twttr("Symbol$%^") == "Symbl$%^"
    assert convert_twttr("Python 3.8") == "Pythn 3.8"


def test_edge_cases():
    # Test with empty string
    assert convert_twttr("") == ""
    # Test with single character
    assert convert_twttr("A") == ""
    assert convert_twttr("b") == "b"
    # Test with spaces
    assert convert_twttr(" ") == " "
    # Test with special characters only
    assert convert_twttr("!@#$%^&*()") == "!@#$%^&*()"
