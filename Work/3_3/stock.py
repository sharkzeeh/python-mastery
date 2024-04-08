# stock.py

from decimal import Decimal

class Stock:

    types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self):
        return self.shares * self.price

    def sell(self, n):
        self.shares -= n

class DStock(Stock):
    types = (str, int, Decimal)


if __name__ == '__main__':
    # (b) Class variables and inheritance
    row = ['AA', '100', '32.20']
    ds = DStock.from_row(row)
    print(ds.price, ds.cost)

    import reader
    portfolio = reader.read_csv_as_instances('../Data/portfolio.csv', Stock)
    print(portfolio)
