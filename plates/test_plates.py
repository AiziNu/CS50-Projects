from plates import is_valid


def test_is_valid_length():
    assert is_valid("AB123") == True
    assert is_valid("AB12325") == False
    assert is_valid("A") == False

def test_is_valid_alphanumeric():
    assert is_valid("AB123") == True
    assert is_valid("AB1 325") == False
    assert is_valid("AB34!") == False

def test_is_valid_starts_alphabetical():
    assert is_valid("AB556") == True
    assert is_valid("1ab325") == False
    assert is_valid("!Abi25") == False

def test_is_valid_all_letters():
    assert is_valid("ABCDEF") == True
