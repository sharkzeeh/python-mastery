# validate.py

import inspect
from functools import wraps

def validated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling', func)
        bound = sig.bind(*args, **kwargs)
        for name, val in annotations.items():
            val.check(bound.arguments[name])
        result = func(*args, **kwargs)
        if retcheck:
            try:
                retcheck.check(result)
            except Exception as e:
                raise TypeError(f'Bad return: {e}')
        return result
    sig = inspect.signature(func)
    annotations = func.__annotations__
    retcheck = annotations.pop('return', None)  # get return type

    return wrapper

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
    @validated
    def add(x: Integer, y: Integer) -> Integer:
        return x + y

    @validated
    def pow(x: Integer, y: Integer) -> Integer:
        return x ** y
    
    add(2, 3)   # ok
    pow(2, 3)   # ok

    try:
        add('2', '3')
    except TypeError as e:
        print(e)
    try:
        pow(2, -1.0)
    except TypeError as e:
        print(e)
