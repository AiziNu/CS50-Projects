from fuel import convert, gauge
import pytest

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("0/1") == 0
    assert convert("1/1") == 100

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("3/2")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"

if __name__ == "__main__":
    pytest.main()
