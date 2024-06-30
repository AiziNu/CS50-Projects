from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar = Jar(-1)

    with pytest.raises(ValueError):
        jar = Jar("not a number")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(3)

def test_capacity():
    jar = Jar(15)
    assert jar.capacity == 15
    jar = Jar()
    assert jar.capacity == 12

def test_size():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(7)
    assert jar.size == 7
    jar.withdraw(4)
    assert jar.size == 3

if __name__ == "__main__":
    pytest.main()

