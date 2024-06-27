import pytest

def test_minutes_to_words():
    assert minutes_to_words(525600) == "five hundred twenty five thousand six hundred"
    assert minutes_to_words(527040) == "five hundred twenty seven thousand forty"  # for a leap year
    assert minutes_to_words(527041) == "five hundred twenty seven thousand forty one"
