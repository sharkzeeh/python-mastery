# stock.py

import csv

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    # (a) Adding a new method
    def sell(self, n):
        self.shares -= n

# (b) Reading a portfolio
def read_portfolio(fname):
    portfolio = []
    with open(fname) as fh:
        rows = csv.reader(fh)
        headers = next(rows)
        for row in rows:
            row[1] = int(row[1])
            row[2] = float(row[2])
            record = Stock(**dict(zip(headers, row)))
            portfolio.append(record)
    return portfolio

def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print(' '.join(['-' * 10] * 3))
    for s in portfolio:
        for s in portfolio:
           print('%10s %10d %10.2f' % (s.name, s.shares, s.price))


if __name__ == '__main__':
    portfolio = read_portfolio('../Data/portfolio.csv')
    print_portfolio(portfolio)
