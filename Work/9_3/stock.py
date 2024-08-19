# stock.py

# (a) Controlling Exported Symbols

from structly import Structure

class Stock(Structure):
    name = String()             # type: ignore
    shares = PositiveInteger()  # type: ignore
    price = PositiveFloat()     # type: ignore

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger): # type: ignore
        self.shares -= nshares


if __name__ == '__main__':
    from structly import read_csv_as_instances
    from structly import create_formatter, print_table
    portfolio = read_csv_as_instances('../Data/portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
