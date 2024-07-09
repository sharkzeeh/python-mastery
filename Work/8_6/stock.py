# stock.py

from structure import Structure

class Stock(Structure):
    name = String()             # type: ignore
    shares = PositiveInteger()  # type: ignore
    price = PositiveFloat()     # type: ignore

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger): # type: ignore
        self.shares -= nshares


# if __name__ == '__main__':
#     s = Stock('GOOG', 100, 490.1)
