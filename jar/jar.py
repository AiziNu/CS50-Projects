

class Jar:
    def __init__(self, capacity=12):
        if not isinstance(n,int) or capacity < 0:
            raise ValueError("Capacity must be non-negative int")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if 


    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
