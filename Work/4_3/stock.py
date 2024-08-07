# stock.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:

    # (c) From Validators to Descriptors
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    _types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    # implements `shares` descriptor __get__
    @property
    def shares(self):
        return self._shares
    
    # overrides `shares` descriptor __set__
    @shares.setter
    def shares(self, value):
        self._shares = PositiveInteger.check(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = PositiveFloat.check(value)

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, n):
        self.shares -= n

    def __repr__(self):
        # Note: The !r format code produces the repr() string
        return f'{type(self).__name__}({self.name!r}, {self.shares!r}, {self.price!r})'

    def __eq__(self, other):
        return isinstance(other, Stock) and \
            ((self.name, self.shares, self.price) ==
             (other.name, other.shares, other.price))


if __name__ == '__main__':
    # (a) Descriptors in action
    #   The execution of __get__() and __set__() 
    #   occurs automatically whenever you access instances.
    s = Stock('GOOG', 100, 490.1)
    print('Stock.__dict__.keys():', Stock.__dict__.keys(), sep='\n')
    shares_desc = Stock.__dict__['shares']
    assert shares_desc.__get__(s) == shares_desc.__get__(s, Stock)
    print(shares_desc.__get__(s))
    shares_desc.__set__(s, 75)
    print(shares_desc.__get__(s))
