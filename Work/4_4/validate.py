# validate.py

# @classmethod allows us to avoid the extra step of
# creating instances which we don't really need

class Validator:
    @classmethod
    def check(cls, value):
        return value
    
class Typed(Validator):
    expected_type = object  # <class 'object'>
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
    
# Multiple inheritance
# Essentially, you're taking existing validators
# and composing them together into new ones
class PositiveInteger(Integer, Positive):
    ...

class PositiveFloat(Float, Positive):
    ...

class NonEmptyString(String, NonEmpty):
    ...


if __name__ == '__main__':
    # (b) Build a Value Checker. Part 1
    n = Integer.check(10)
    print(n)
    s = String.check('10')
    print(s)
    try:
        Integer.check('10')
    except TypeError as e:
        print(e)

    def add(x, y):
        Integer.check(x)
        Integer.check(y)
        return x + y

    sm = add(2, 2)
    print(sm)
    try:
        add(2, '2')
    except TypeError as e:
        print(e)

    # (b) Build a Value Checker. Part 2
    n = PositiveInteger.check(10)
    print(n)
    try:
        PositiveInteger.check('10')
    except TypeError as e:
        print(e)
    try:
        PositiveInteger.check(-10)
    except ValueError as e:
        print(e)

    s = NonEmptyString.check('hello')
    print(s)
    try:
        NonEmptyString.check('')
    except ValueError as e:
        print(e)
