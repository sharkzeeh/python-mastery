# validate.py

import inspect

# (a) Creating a Callable Object
# (b) Enforcement


class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Calling', self.func)
        sig = inspect.signature(self.func)
        bound = sig.bind(*args, **kwargs)
        # from exercise example: bound args = (10,)
        # missing `self` -> FAILS in `stock.py` ?
        for name, val in self.func.__annotations__.items():
            val.check(bound.arguments[name])

        result = self.func(*args, **kwargs)
        return result

class Validator:

    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)

class PositiveInteger(Integer, Positive):
    ...

class PositiveFloat(Float, Positive):
    ...

class NonEmptyString(String, NonEmpty):
    ...


if __name__ == '__main__':
    # (a) Creating a Callable Object
    def add(x, y):
        Integer.check(x)
        Integer.check(y)
        return x + y
    
    # add = ValidatedFunction(add)
    # add(2, 3)
    # Calling <function add at ...>
    # 5

    # (b) Enforcement
    def add(x: Integer, y:Integer):
        return x + y

    add = ValidatedFunction(add)
    add(2, 3)
    # bound.arguments == {'x': 2, 'y': 3}
