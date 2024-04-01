# stock.py

import csv

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, n):
        self.shares -= n

def read_portfolio(fname):
    portfolio = []
    with open(fname) as fh:
        rows = csv.reader(fh)
        headers = next(rows)
        for row in rows:
            record = Stock(row[0], int(row[1]), float(row[2]))
            portfolio.append(record)
    return portfolio

def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print(' '.join(['-' * 10] * 3))
    for s in portfolio:
        for s in portfolio:
           print('%10s %10d %10.2f' % (s.name, s.shares, s.price))


if __name__ == '__main__':
    # (d) Bound Methods
    s = Stock('GOOG', 100, 490.10)
    c = s.cost
    print(c())
    s.shares = 75
    print(c())  # modified
    print(c.__self__)
    print(c.__func__)
    assert c.__func__(c.__self__) == Stock.cost(s)
