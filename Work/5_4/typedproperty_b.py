# typedproperty.py

# (b) Closures as a code generator
def typedproperty(name, expected_type):

    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    # return property object
    return value

def String(name):
    return typedproperty(name, str)

def Integer(name):
    return typedproperty(name, int)

def Float(name):
    return typedproperty(name, float)


if __name__ == '__main__':
    class Stock:
        name = String('name')
        shares = Integer('shares')
        price = Float('price')
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

    s = Stock('GOOG', 100, 490.1)
    # throws type error
    try:
        s.shares = '50'
    except TypeError as e:
        print(e)
    print(s.shares)
