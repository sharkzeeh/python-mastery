# structure.py

# (e) Method Argument Checking

# Remember that @validated decorator you wrote in the last part?
# Let's modify the @validate_attributes decorator so that any method
# in the class with annotations gets wrapped by @validated
# automatically. This allows you to put enforced annotations on methods
# such as the sell() method:

import inspect
from validate import Validator, validated

def validate_attributes(cls):
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
        elif callable(val) and val.__annotations__:
            setattr(cls, name, validated(val))

    # Collect all of the field names
    cls._fields = tuple([v.name for v in validators])

    # Collect type conversions.
    # The lambda x:x is an identity function
    # that's used in case no expected_type is found.
    cls._types = tuple([ getattr(v, 'expected_type', lambda x: x)
                   for v in validators ])

    # Create the __init__ method
    if cls._fields:
        cls.create_init()

    return cls

class Structure:
    _fields = ()
    _types = ()

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)

    @classmethod
    def create_init(cls):
        argstr = ','.join(cls._fields)
        code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            code += f'  self.{name} = {name}\n'
        locs = locals()
        exec(code, locs)
        cls.__init__ = locs['__init__']

    def __setattr__(self, name, value):
        if name not in self._fields and not name.startswith('_'):
            raise AttributeError('No attribute %s' % (name, ))
        super().__setattr__(name, value)

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__,
                           ', '.join((repr(getattr(self, field)) for field in self._fields))
                           )

    @classmethod
    def from_row(cls, row):
        rowdata = [func(val) for func, val in zip(cls._types, row)]
        return cls(*rowdata)
