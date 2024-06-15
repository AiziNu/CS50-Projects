from bank import value

def test_value_hello():
    assert value("hello") == 0

def test_value_casesensetive():
    assert value("HeLlo") == 0

def test_value_h():
    assert value('hi') == 20

def test_value_h_casesensetive():
    assert value('Hey') == 20

def test_value_other():
    assert value("goodbye") == 100

def test_value_emty_value():
    assert value("") == 100

