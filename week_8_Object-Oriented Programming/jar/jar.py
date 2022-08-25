class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0


    def __str__(self):
        return "🍪" * self._size


    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Exceed capacity")
        if (n + self._size) > self.capacity:
            raise ValueError("Exceed capacity")
        self._size += n


    def withdraw(self, n):
        if n > self.capacity:
            raise ValueError("There are not enough coockies to withdrow")
        if (self._size - n) < 0:
            raise ValueError("There are not enough coockies to withdrow ")
        self._size -= n


    @property
    def size(self):
        return self._size


    @property
    def capacity(self):
        return self._capacity


    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity should be non-negative value")
        self._capacity = value
