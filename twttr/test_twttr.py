from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("rhythm") == "rhythm"

def test_shorten_mixed_case():
    assert shorten("Twitter") == "Twttr"

def test_shorten_all_vowels():
    assert shorten("AEIOUaeiou") == ""

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_sentence():
    sentence = "Hello, World!"
    expected = "Hll, Wrld!"
    assert shorten(sentence) == expected


