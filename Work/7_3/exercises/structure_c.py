# structure.py

# (c) Applying Decorators via Inheritance

# Having to specify the class decorator itself is kind of annoying.
# Modify the `Structure` class with the following __init_subclass__() method:

from validate import Validator

def validate_attributes(cls):
    validators = []
    for _, val in vars(cls).items():    # ... in cls.__dict__.items():
        if isinstance(val, Validator):
            validators.append(val)
    cls._fields = [val.name for val in validators]

    if cls._fields:
        cls.create_init()
    return cls

class Structure:
    _fields = ()

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
