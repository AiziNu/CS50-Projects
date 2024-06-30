import pytest
from datetime import date
from seasons import calculate_age_in_minutes

def test_calculate_age_in_minutes():
    assert calculate_age_in_minutes(date(2000, 1, 1), date(2001, 1, 1)) == 366 * 24 * 60  # Includes a leap year
    assert calculate_age_in_minutes(date(2020, 1, 1), date(2021, 1, 1)) == 366 * 24 * 60  # Leap year check
    assert calculate_age_in_minutes(date(2021, 1, 1), date(2022, 1, 1)) == 365 * 24 * 60  # Non-leap year check
    assert minutes_to_words(525600) == "five hundred twenty five thousand six hundred"
    assert minutes_to_words(527040) == "five hundred twenty seven thousand forty"  # for a leap year
    assert minutes_to_words(527041) == "five hundred twenty seven thousand forty one"

# Running the tests
if __name__ == "__main__":
    pytest.main()
