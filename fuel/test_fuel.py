from fuel import convert, gauge
import pytest

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("0/1") == 0


def test_convert_invalid():
     with pytest.raises(ValueError):
        assert convert("cat/dog")
        assert convert("cat")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

if __name__ == "__main__":
    pytest.main()
