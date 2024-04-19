# typedproperty.py

class SpecialProperty(property):
    def __set_name__(self, owner, name):
        self.private_name = '_' + name
        super().__set_name__(owner, name)

def typedproperty(expected_type):

    @SpecialProperty
    def value(self):
        return getattr(self, value.private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, value.private_name, val)

    return value

def String():
    return typedproperty(str)

def Integer():
    return typedproperty(int)

def Float():
    return typedproperty(float)


if __name__ == '__main__':
    class Stock:
        name = String()
        shares = Integer()
        price = Float()
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

    s = Stock('GOOG', 100, 490.1)
    try:
        s.shares = '50'
    except TypeError as e:
        print(e)
    print(s.shares)
