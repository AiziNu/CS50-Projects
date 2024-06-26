from working import convert
import pytest

def test_valid_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("1 PM to 1 AM") == "13:00 to 01:00"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"

def test_invalid_times():
    with pytest.raises(ValueError):
        convert("13:00 PM to 1:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 5")
    with pytest.raises(ValueError):
        convert("random text")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")

if __name__ == "__main__":
    pytest.main()

