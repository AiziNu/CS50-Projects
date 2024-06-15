from twttr import convert_twttr

def test_no_vowels():
    assert convert_twttr("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"

def test_only_vowels():
    assert convert_twttr("AEIOUaeiou") == ""

def test_mixed_case():
    assert convert_twttr("hello") == "hll"
    assert convert_twttr("HELLO") == "HLL"
    assert convert_twttr("hElLo") == "hlL"

def test_numbers_and_special_chars():
    assert convert_twttr("12345") == "12345"
    assert convert_twttr("!@#$%") == "!@#$%"
    assert convert_twttr("Python 3.8") == "Pythn 3.8"

def test_edge_cases():
    assert convert_twttr("") == ""
    assert convert_twttr("A") == ""
    assert convert_twttr("b") == "b"
    assert convert_twttr(" ") == " "
    assert convert_twttr("a e i o u") == " "
    assert convert_twttr("!@#$%^&*()") == "!@#$%^&*()"

def test_mixed_content():
    assert convert_twttr("Python Programming is Fun!") == "Pythn Prgrmmng s Fn!"
    assert convert_twttr("Test 123!@#") == "Tst 123!@#"

if __name__ == "__main__":
    import pytest
    pytest.main()
