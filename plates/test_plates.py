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
    assert is_valid("ABFGTR") == True
    assert is_valid("1Ab325") == False
    assert is_valid("0Abi25") == False

def test_is_valid_all_letters():
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("A1B") == False

def test_is_valid_numbers_not_in_middle():
    assert is_valid("AB123") == True
    assert is_valid("A1B23") == False
    assert is_valid("AB12C") == False

def test_is_valid_no_leading_zero():
    assert is_valid("AB123") == True
    assert is_valid("AB012") == False
    assert is_valid("A0123B") == False
