# mutint.py

class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

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

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f'MutInt({self.value!r})'
    
    def __format__(self, fmt):
        return format(self.value, fmt)


if __name__ == '__main__':
    # b
    a = MutInt(3)
    print(a)
    print(repr(a))
    print(f'The value is {a:*^10d}')
    a.value = 42
    print(a)
    # c
    a + 10
    10 + a
