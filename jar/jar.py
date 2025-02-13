

class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity,int) or capacity < 0:
            raise ValueError("Capacity must be non-negative int")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if not isinstance(n,int) or n< 0:
            raise ValueError('Number of cookies must be non-negative int')
        if self._cookies + n > self._capacity:
            raise ValueError("Exceeds cookie jar")
        self._cookies += n


    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError('Number of cookies withdraw must be non-negative int')
        if self._cookies - n < 0:
            raise ValueError("Not enough cookies in the jar")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies
