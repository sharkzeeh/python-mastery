# A common use of descriptors is in describing data
# e.g., Object Relational Mapping, etc.

class String:
    def __init__(self, name, maxlen):
        ...
class Real:
    def __init__(self, name):
        ...
class Integer:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, cls):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        instance.__dict__[self.name] = value

class Stock:
    name   = String('name', maxlen=8)
    shares = Integer('shares')
    price  = Real('price')


if __name__ == '__main__':
    s = Stock()
    s.shares = 42
    print(s.__dict__)   # {'shares': 42}
    print(s.shares)
    try:
        s.shares = 42.0
    except TypeError as e:
        print(e)
