# mymeta.py

# (a) Create your first metaclass

# The main power of a metaclass is that it gives a programmer the ability
# to capture details about classes just prior to their creation. For
# example, in the __new__() method, you are given all of the
# basic details including the name of the class, base classes, and
# methods data. If you inspect this data, you can perform various
# types of diagnostic checks. If you're more daring, you can modify the
# data and change what gets placed in the class definition when it is
# created.

class mytype(type):
    @staticmethod
    def __new__(meta, name, bases, __dict__):
        print("Creating class :", name)
        print("Base classes   :", bases)
        print("Attributes     :", list(__dict__))
        return super().__new__(meta, name, bases, __dict__) # type: ignore

class myobject(metaclass=mytype):
    pass

class Stock(myobject):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
    def sell(self, nshares):
        self.shares -= nshares

class MyStock(Stock):
    pass

if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.1)
    print(s)
    ms = MyStock('GOOG', 100, 490.1)
    print(ms)
