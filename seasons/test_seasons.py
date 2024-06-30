import pytest
from datetime import date, datetime
from seasons import calculate_age_in_minutes, format_minutes_in_words

def test_calculate_age_in_minutes():
    assert calculate_age_in_minutes("2000-01-01") == int((datetime.combine(date.today(), datetime.min.time()) - datetime(2000, 1, 1)).total_seconds() // 60)

def test_calculate_age_in_minutes_invalid_format():
    assert calculate_age_in_minutes("01-01-2000") is None
    assert calculate_age_in_minutes("2000/01/01") is None

def test_format_minutes_in_words():
    assert format_minutes_in_words(525600) == "Five hundred twenty five thousand six hundred"
    assert format_minutes_in_words(1051200) == "One million fifty one thousand two hundred"
    assert format_minutes_in_words(2629440) == "Two million six hundred twenty nine thousand four hundred forty"
    assert format_minutes_in_words(6092640) == "Six million ninety two thousand six hundred forty"
    assert format_minutes_in_words(806400) == "Eight hundred six thousand four hundred"

if __name__ == "__main__":
    pytest.main()
