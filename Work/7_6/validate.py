# validate.py

import inspect
from functools import wraps

def validated(func):
    sig = inspect.signature(func)
    annotations = func.__annotations__

    # Get the return annotation (if any)
    retcheck = annotations.pop('return', None)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        errors = []

        # Enforce argument checks
        for name, val in annotations.items():
            try:
                val.check(bound.arguments[name])
            except Exception as e:
                errors.append(f'    {name}: {e}')

        if errors:
            raise TypeError('Bad arguments\n' + '\n'.join(errors))

        result = func(*args, **kwargs)

        # Enforce return check (if any)
        if retcheck:
            try:
                retcheck.check(result)
            except Exception as e:
                raise TypeError(f'Bad return: {e}')
        return result

    return wrapper

def enforce(**annotations):
    # Get the return annotation (if any)
    retcheck = annotations.pop('return_', None)

    def decorate(func):
        sig = inspect.signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound = sig.bind(*args, **kwargs)
            errors = []

            for name, val in annotations.items():
                try:
                    val.check(bound.arguments[name])
                except Exception as e:
                    errors.append(f'    {name}: {e}')
            
            if errors:
                raise TypeError('Bad Arguments\n' + '\n'.join(errors))

            result = func(*args, **kwargs)

            if retcheck:
                try:
                    retcheck.check(result)
                except Exception as e:
                    raise TypeError(f'Bad return: {e}')
            return result
        return wrapper
    return decorate

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
    
    # Collect all derived classes into a dict
    validators = {}
    @classmethod
    def __init_subclass__(cls):
        cls.validators[cls.__name__] = cls
        # Validator.validators[cls.__name__] = cls

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

# Validator.validators
    # {'Float': <class 'validate.Float'>,
    # 'Integer': <class 'validate.Integer'>,
    # 'NonEmpty': <class 'validate.NonEmpty'>,
    # 'NonEmptyString': <class 'validate.NonEmptyString'>,
    # 'Positive': <class 'validate.Positive'>,
    # 'PositiveFloat': <class 'validate.PositiveFloat'>,
    # 'PositiveInteger': <class 'validate.PositiveInteger'>,
    # 'String': <class 'validate.String'>,
    # 'Typed': <class 'validate.Typed'>}
