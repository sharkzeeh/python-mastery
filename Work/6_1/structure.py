# structure.py

class Structure:
    _fields = ()
    # (a) Simplified Data Structures
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected %d arguments' % (len(self._fields), ))
        for field, arg in zip(self._fields, args):
            setattr(self, field, arg)
            # super().__setattr__(field, arg) # will not call Structure.__setattr__

    # (c) Restricting Attribute Names
    def __setattr__(self, name, value):
        if name not in self._fields and not name.startswith('_'):
            raise AttributeError('No attribute %s' % (name, ))
        super().__setattr__(name, value)

    # (b) Making a Useful Representation
    def __repr__(self):
        # return f"{type(self).__name__}({', '.join(repr(getattr(self, field)) for field in self._fields)})"
        return '%s(%s)' % (type(self).__name__,
                           ', '.join((repr(getattr(self, field)) for field in self._fields))
                           )

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

class Date(Structure):
    _fields = ('year', 'month', 'day')


if __name__ == '__main__':
    # (a) Simplified Data Structures
    s = Stock('GOOG', 100, 490.1)
    print(s.name, s.shares, s.price)
    # throws error
    try:
        se = Stock('AA', 50)
    except TypeError as e:
        print(e)
    
    # (b) Making a Useful Representation
    print(s)

    # (c) Restricting Attribute Names
    s.shares = 50
    s._shares = 100
    try:
        s.share = 50
    except AttributeError as e:
        print(e)

    print(help(s.__init__))  # useless __init__ signature
