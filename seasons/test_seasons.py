from datetime import date
from seasons import calculate_age_in_minutes, convert_number_to_words

def test_calculate_age_in_minutes():
    assert calculate_age_in_minutes(date(2000, 1, 1), date(2020, 1, 1)) == 10540800
    assert calculate_age_in_minutes(date(2023, 6, 24), date(2024, 6, 24)) == 527040
    assert calculate_age_in_minutes(date(2023, 2, 28), date(2023, 3, 1)) == 1440

def test_convert_number_to_words():
    assert convert_number_to_words(10540800) == "ten million five hundred forty thousand eight hundred minutes"
    assert convert_number_to_words(527040) == "five hundred twenty-seven thousand forty minutes"
    assert convert_number_to_words(1440) == "one thousand four hundred forty minutes"

if __name__ == "__main__":
    import pytest
    pytest.main()
