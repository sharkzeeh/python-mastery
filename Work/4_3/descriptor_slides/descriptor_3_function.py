# Descriptors and Functions

# Functions are descriptors where __get__() 
# creates the bound method object

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price


if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.10)
    # class attribute lookup
    value = Stock.__dict__['cost']  # function-descriptor
    print(value)
    # descriptor check
    assert hasattr(value, '__get__') == True
    # descriptor invocation
    result = value.__get__(s, Stock)
    print(result)
    print(result())
