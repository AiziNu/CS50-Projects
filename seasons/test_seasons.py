import pytest
from datetime import date, datetime
from seasons import calculate_age_in_minutes, format_minutes_in_words

def test_calculate_age_in_minutes():
    assert calculate_age_in_minutes("2000-01-01") == (datetime.combine(date.today(), datetime.min.time()) - datetime(2000, 1, 1)).total_seconds() // 60

def test_calculate_age_in_minutes_invalid_format():
    assert calculate_age_in_minutes("01-01-2000") is None
    assert calculate_age_in_minutes("2000/01/01") is None

def test_format_minutes_in_words():
    assert format_minutes_in_words(525600) == "five hundred twenty five thousand six hundred"
    assert format_minutes_in_words(1051200) == "one million fifty one thousand two hundred"

if __name__ == "__main__":
    pytest.main()
