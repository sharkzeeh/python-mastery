# stock.py

from structure import Structure

class Stock(Structure):

    def __init__(self, name, shares, price):
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

if __name__ == '__main__':
    # (c) Putting it Together
    Stock.set_fields()

    s = Stock(name='GOOG', price=490.1, shares=50)
    import inspect
    sig = inspect.signature(Stock)
    print(repr(sig))                # <Signature (name, shares, price)>
    print(tuple(sig.parameters))    # ('name', 'shares', 'price')
    print(s)
