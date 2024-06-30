import pytest
from seasons import minutes_lived


def main():
    test_1()
    test_2()

def test_1():
    assert  minutes_lived(1997-03-05) == "Fourteen million, three hundred sixty-nine thousand, seven hundred sixty minutes"
    assert  minutes_lived(1997-03-05) == "Fourteen million, three hundred sixty-nine thousand, seven hundred sixty minutes"

# Running the tests
if __name__ == "__main__":
    pytest.main()
