import pytest
from um import count

def test_single_um():
    assert count("um") == 1

def test_um_with_punctuation():
    assert count("um,") == 1

def test_multiple_ums():
    assert count("um, um, um") == 3

def test_um_at_start():
    assert count("Um, hello world") == 1

def test_um_at_end():
    assert count("Hello world, um") == 1

def test_um_middle_of_sentence():
    assert count("Hello, um, world") == 1

def test_um_as_substring():
    assert count("yummy") == 0

def test_no_um():
    assert count("Hello world") == 0

def test_um_case_insensitive():
    assert count("Um um UM um") == 4

# Running the tests
if __name__ == "__main__":
    pytest.main()
