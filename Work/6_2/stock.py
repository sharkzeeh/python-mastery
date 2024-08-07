# stock.py

from structure import Structure

class Stock(Structure):

    # This gave a useful signature, but now the class is just weird because
    # the user has to provide both the _fields variable and the __init__() method.
    _fields = ('name', 'shares', 'price')
    def __init__(self, name, shares, price):
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

if __name__ == '__main__':
    s = Stock(name='GOOG', price=490.1, shares=50)
    assert hasattr(s, '_init')
    print(s.name, s.shares, s.price)
    print(help(Stock))  # better help - improved __init__ signature
