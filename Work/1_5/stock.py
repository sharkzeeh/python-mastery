class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price


if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.10)
    print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
    print(f'{s.name:>10} {s.shares:>10d} {s.price:>10.2f}')
