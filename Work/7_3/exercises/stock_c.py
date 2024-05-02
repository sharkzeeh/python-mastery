# stock.py

# (c) Applying Decorators via Inheritance

from structure_c import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


if __name__ == '__main__':
    s = Stock(name='GOOG', price=490.1, shares=50)
    print(s)