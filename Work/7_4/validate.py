# validate.py

# (c) Making a lot of classes

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

class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str) ]

globals().update((name,
                  type(name, (Typed,), {'expected_type': ty}))
                 for name, ty in _typed_classes)


if __name__ == '__main__':
    # print(globals())
    integer = Integer() # type: ignore
    res = integer.check(5)
    print(res)
