# (a) Class creation

def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

def sell(self, nshares):
    self.shares -= nshares

methods = {
    '__init__': __init__,
    'cost': cost,
    'sell': sell
}

Stock = type('Stock', (object,), methods)

#  A class is really nothing more than 
# a name, a tuple of base classes, and a dictionary holding
# all of the class contents. type() is a constructor that
# creates a class for you if you supply these three parts.

if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.10)
    print(s.name)
    print(s.cost())
    s.sell(25)
    print(s.shares)
