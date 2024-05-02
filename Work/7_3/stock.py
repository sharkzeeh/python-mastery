# stock.py

# (e) Method Argument Checking

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares


if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.1)
    s.sell(25)
    s.sell(-25)
