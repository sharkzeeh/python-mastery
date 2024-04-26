# structure.py

import sys

class Structure:
    _fields = ()
    
    # (c) Putting it Together
    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    def __setattr__(self, name, value):
        if name not in self._fields and not name.startswith('_'):
            raise AttributeError('No attribute %s' % (name, ))
        super().__setattr__(name, value)

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__,
                           ', '.join((repr(getattr(self, field)) for field in self._fields))
                           )

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

class Date(Structure):
    _fields = ('year', 'month', 'day')


if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.1)
    print(s.name, s.shares, s.price)
