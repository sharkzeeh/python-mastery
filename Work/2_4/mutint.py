# mutint.py

from functools import total_ordering

# @total_ordering fills in the missing comparison methods
# for you as long as you minimally provide 
# an equality operator and one of the other relations.

@total_ordering
class MutInt:

    # (a) Mutable Integers
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    # (b) Fixing output
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f'MutInt({self.value!r})'
    
    def __format__(self, fmt):
        return format(self.value, fmt)

    # (c) Math Opearations
    def __add__(self, other):
        if isinstance(other, int):
            return self.value + other
        elif isinstance(other, MutInt):
            return self.value + other.value
        else:
            return NotImplemented

    __radd__ = __add__    # Reversed operands

    def __iadd__(self, other):
        if isinstance(other, int):
            self.value += other
            return self
        elif isinstance(other, MutInt):
            self.value += other.value
            return self
        else:
            return NotImplemented

    # (d) Comparisons
    # Note: @total_oerdering
    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    # (e) Conversions
    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)

    __index__ = __int__     # Make indexing work

if __name__ == '__main__':
    # b
    a = MutInt(3)
    print(a)
    print(repr(a))
    print(f'The value of `a` is {a:*^10d}')
    a.value = 42
    print('a =', a)
    # c
    a += 10
    a = 10 + a
    print('a =', a)
    # d
    a = MutInt(3)
    b = MutInt(3)
    c = MutInt(4)
    assert a == b
    assert a < c and a <= c
    # e
    print(int(a))
    print(float(a))
    names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
    print(names[a]) # won't work without __index__ method
