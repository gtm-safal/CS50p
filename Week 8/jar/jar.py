class Jar:
    def __init__(self, capacity=12):
       if capacity<0:
           raise ValueError
       self.cap = capacity
       self.n = 0

    def __str__(self):
        return "🍪" * self.n

    def deposit(self, n):
        if self.n + n > self.cap:
            raise ValueError
        self.n += n

    def withdraw(self, n):
        if n > self.n:
            raise ValueError
        self.n -= n


    @property
    def capacity(self):
        return self.cap

    @property
    def size(self):
        return self.n
