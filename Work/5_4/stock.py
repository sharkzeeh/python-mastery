# stock.py

# (b) Closures as a code generator
from typedproperty import String, Integer, Float

class Stock:

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

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
    def cost(self):
        return self.shares * self.price

    def sell(self, n):
        self.shares -= n

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.shares:d}, {self.price:.1f})'

    def __eq__(self, other):
        return isinstance(other, Stock) and \
            ((self.name, self.shares, self.price) ==
             (other.name, other.shares, other.price))


if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.1)
    # throws type error
    try:
        s.shares = '50'
    except TypeError as e:
        print(e)