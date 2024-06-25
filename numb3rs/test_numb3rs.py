from numb3rs import validate

def test_valid_addresses():
    assert validate("127.0.0.1") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True


def test_invalid_addresses():
    assert validate("75.456.76.65") == False
    assert validate("192.168.0") == False
    assert validate("192.168.0.abc") == False
    assert validate("") == False
    assert validate("123.045.067.089") == False  # Leading zeros invalid

def test_edge_cases():
    assert validate("0.0.0.256") == False
    assert validate("0.0.0.-1") == False
    assert validate(" 0.0.0.0") == False
