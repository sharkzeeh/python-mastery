class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price


if __name__ == '__main__':
    goog = Stock('GOOG', 100, 490.10)
    ibm  = Stock('IBM', 50, 91.23)
    # (c) The role of classes
    cost = goog.cost()
    print(cost)

    cost = Stock.__dict__['cost'](goog)
    print(cost)

    Stock.spam = 42
    assert 'spam' not in goog.__dict__
    assert 'spam' in Stock.__dict__
