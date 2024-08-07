# stock.py

from structure import Structure

class Stock(Structure):

    # (b) Creating an __init__() function
    ## removed __init__ function
    ## added _fields
    _fields = ('name', 'shares', 'price')

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

Stock.create_init()


if __name__ == '__main__':
    s = Stock(name='GOOG', price=490.1, shares=50)
    print(s)
