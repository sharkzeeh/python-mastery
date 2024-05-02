# structure.py

# (d) Row Conversion
# Modify the @validate_attributes decorator so that it examines the
# various validators for an expected_type attribute and uses it to
# fill in the _types variable above.

from validate import Validator

def validate_attributes(cls):
    validators = []
    for _, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
    cls._fields = [val.name for val in validators]
    cls._types = [val.expected_type for val in validators]

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

    # (d) Row Conversion
    _types = ()

    @classmethod
    def from_row(cls, row):
        rowdata = [func(val) for func, val in zip(cls._types, row)]
        return cls(*rowdata)
