# structure.py
# (b) Adding Iteration to Objects
# (c) The Surprising Power of Iteration

from collections import ChainMap
from validate import Validator, validated

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(metacls, clsname, bases, methods):
        # metaclass - metaclass StructureMeta
        # clsname - string e.g., Stock, Structure
        methods = methods.maps[0]   # drop validator dictionary
        return super().__new__(metacls, clsname, bases, methods)  # type: ignore

class Structure(metaclass=StructureMeta):
    _fields = ()
    _types = ()

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError('No attribute %s' % name)

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__,
                           ', '.join(repr(getattr(self, name)) for name in self._fields))

    @classmethod
    def from_row(cls, row):
        rowdata = [ func(val) for func, val in zip(cls._types, row) ]
        return cls(*rowdata)

    @classmethod
    def create_init(cls):
        '''
        Create an __init__ method from _fields
        '''
        args = ','.join(cls._fields)
        code = f'def __init__(self, {args}):\n'
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'
        locs = {}
        exec(code, locs)
        cls.__init__ = locs['__init__']

    @classmethod
    def __init_subclass__(cls):
        # Apply the validated decorator to subclasses
        validate_attributes(cls)

    # (b) Adding Iteration to Objects
    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)

    # (c) The Surprising Power of Iteration
    def __eq__(self, other):
        return isinstance(other, type(self)) and \
            tuple(self) == tuple(other)


def validate_attributes(cls):
    '''
    Class decorator that scans a class definition for Validators
    and builds a _fields variable that captures their definition order.
    '''
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

        # Apply validated decorator to any callable with annotations
        elif callable(val) and val.__annotations__:
            setattr(cls, name, validated(val))

    # Collect all of the field names
    cls._fields = tuple([v.name for v in validators])

    # Collect type conversions. The lambda x:x is an identity
    # function that's used in case no expected_type is found.
    cls._types = tuple([ getattr(v, 'expected_type', lambda x: x)
                   for v in validators ])

    # Create the __init__ method
    if cls._fields:
        cls.create_init()

    return cls

def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure,), validators)
    return cls


if __name__ == '__main__':
    # NOTE: under the hood Stock uses Structure class
    # => Stock class receives __iter__ method

    # (b) Adding Iteration to Objects
    from stock import Stock
    s = Stock('GOOG', 100, 490.1)
    for val in s:
        print(val)
    # GOOG
    # 100
    # 490.1

    # (c) The Surprising Power of Iteration
    # Python uses iteration in ways you might not expect.
    # Once you've added __iter__() to the Structure class,
    # you'll find that it is easy to do all sorts of new
    # operations. For example, conversions to sequences and unpacking
    a = Stock('GOOG', 100, 490.1)
    b = Stock('GOOG', 100, 490.1)
    assert a == b

    # NOTE: without __iter__ method you would get
    # tuple(self) == tuple(other)
    # TypeError: 'Stock' object is not iterable
