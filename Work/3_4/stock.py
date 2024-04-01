# stock.py

from decimal import Decimal

class Stock:
    
    __slots__ = ['name', '_shares', '_price']

    _types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f'Expected {self._types[1].__name__}')
        if value < 0:
            raise ValueError('shares must be >= 0')
        self._shares = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f'Expected {self._types[2].__name__}')
        if value < 0:
            raise ValueError('price must be >= 0')
        self._price = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, n):
        self.shares -= n

class DStock(Stock):
    _types = (str, int, Decimal)


if __name__ == '__main__':
    # (b) Properties for computed attributes
    s = Stock('GOOG', 100, 490.1)
    print(s.cost)

    # (c) Enforcing Validation Rules
    try:
        s.shares = -10
    except ValueError as e:
        print(e)

    # (d) Adding __slots__
    try:
        s.spam = 42
    except AttributeError as e:
        print(e)
