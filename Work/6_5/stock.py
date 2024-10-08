# stock.py

import functools
import validate
import inspect

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    # (c) Use as a Method (Challenge)
    # def sell(self, nshares: validate.Integer):
    #     self.shares -= nshares
    # sell = validate.ValidatedFunction(sell)     # Fails

    # also works if defined outside of class definition
    def validated(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            other = validate.ValidatedFunction(func)
            return other(*args, **kwargs)
        return wrapper
    
    @validated
    def sell(self, nshares: validate.Integer):
        # >>> print(inspect.signature(self.sell))
        # (nshares: validate.Integer)
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
