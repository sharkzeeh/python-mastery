class SimpleStock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price


if __name__ == '__main__':
    goog = SimpleStock('GOOG', 100, 490.10)
    ibm  = SimpleStock('IBM', 50, 91.23)
    # (c) The role of classes
    cost = goog.cost()
    print(cost)

    cost = SimpleStock.__dict__['cost'](goog)
    print(cost)

    SimpleStock.spam = 42
    assert 'spam' not in goog.__dict__
    assert 'spam' in SimpleStock.__dict__
    