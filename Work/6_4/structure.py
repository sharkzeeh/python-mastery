# structure.py

# (b) Using Class Decorators to Fill in Details

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
