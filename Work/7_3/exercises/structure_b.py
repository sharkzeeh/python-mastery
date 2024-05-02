# structure.py

# (b) Using Class Decorators to Fill in Details

# An annoying aspect of the code is there are extra details such as
# _fields variable and the final step of Stock.create_init().
# A lot of this could be packaged into a class decorator instead.


# This code relies on the fact that class dictionaries are ordered
# starting in Python 3.6. Thus, it will encounter the different
# Validator descriptors in the order that they're listed. Using this
# order, you can then fill in the _fields variable.

from validate import Validator

def validate_attributes(cls):
    validators = []
    for _, val in vars(cls).items():    # ... in cls.__dict__.items():
        if isinstance(val, Validator):
            validators.append(val)
    # fills cls._fields automatically
    cls._fields = [val.name for val in validators]

    if cls._fields:
        cls.create_init()
    return cls

class Structure:
    _fields = ()

    @classmethod
    def create_init(cls):
        argstr = ','.join(cls._fields)
        code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            code += f'  self.{name} = {name}\n'
        locs = locals()
        exec(code, locs)                # creates __init__ function inside `create_init`
        cls.__init__ = locs['__init__'] # won't work without exec(code, locs)

    def __setattr__(self, name, value):
        if name not in self._fields and not name.startswith('_'):
            raise AttributeError('No attribute %s' % (name, ))
        super().__setattr__(name, value)

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__,
                           ', '.join((repr(getattr(self, field)) for field in self._fields))
                           )
