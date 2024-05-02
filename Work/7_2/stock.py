# stock.py

import validate

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price
    
    @validate.validated
    def sell(self, nshares: validate.Integer):
        self.shares -= nshares


if __name__ == '__main__':
    s = Stock(name='GOOG', price=490.1, shares=50)
    print('Number of shares:', s.shares)
    print('Selling 10 shares ...')
    s.sell(10)
    s.sell(10)
    try:
        s.sell(10.0)    # Fails
    except TypeError as e:
        print(e)
    print('Number of shares:', s.shares)
