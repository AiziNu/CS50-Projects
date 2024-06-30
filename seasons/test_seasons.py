import pytest
from seasons import minutes_lived


def main():
    test_1()
    test_2()

def test_1():
    assert minutes_lived(1997, 3, 5) == "Fourteen million, three hundred sixty-nine thousand, seven hundred sixty minutes"
    assert minutes_lived(1983, 11, 11) == "Twenty-one million, three hundred seventy-two thousand, four hundred eighty minutes"

def test_2():
    assert minutes_lived(19, 3, 1989) == "Invalid date"


# Running the tests
if __name__ == "__main__":
    pytest.main()
