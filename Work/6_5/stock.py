# stock.py
import functools
import validate

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: validate.Integer):
        self.shares -= nshares

    # (c) Use as a Method (Challenge)
    sell = validate.ValidatedFunction(sell)     # Fails


if __name__ == '__main__':
    s = Stock(name='GOOG', price=490.1, shares=50)
    print('Number of shares:', s.shares)
    print('Sell 10 shares')
    s.sell(10)
    print('Number of shares:', s.shares)