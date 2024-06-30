from seasons import calculate_age_in_minutes
from datetime import date

def test_calculate_minutes_since_birth():
    # Test for a date with known difference
    birth_date = date(2000, 1, 1)
    today_date = date(2023, 1, 1)
    delta = today_date - birth_date
    expected_minutes = delta.days * 24 * 60
    assert calculate_minutes_since_birth(birth_date) == expected_minutes

def test_calculate_minutes_since_birth_with_leap_year():
    # Test for a date range that includes a leap year
    birth_date = date(2020, 1, 1)
    today_date = date(2023, 1, 1)
    delta = today_date - birth_date
    expected_minutes = delta.days * 24 * 60
    assert calculate_minutes_since_birth(birth_date) == expected_minutes

if __name__ == "__main__":
    test_calculate_minutes_since_birth()
    test_calculate_minutes_since_birth_with_leap_year()
    print("All tests passed!")
