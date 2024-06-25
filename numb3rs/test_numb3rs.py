from numb3rs import validate

def test_valid_addresses():
    assert validate("127.0.0.1") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.0") == True



def test_invalid_addresses():
    assert validate("275.3.6.28") == False
    assert validate("192.168.0") == False
    assert validate("192.168.0.abc") == False

def test_edge_cases():
    assert validate("0.0.0.256") == False
    assert validate("0.0.0.-1") == False
    assert validate("cat") == False
