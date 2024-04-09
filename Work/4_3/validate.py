# validate.py

class Validator:
    # (c) From Validators to Descriptors
    def __init__(self, name=None):
        self.name = name

    # def __get__(self, instance, cls=None):
    #     if instance is None:
    #         return self
    #     return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
        # self examples: Integer(), PositiveFloat(), NonEmptyString() ...

    # NOTE: The lack of the __get__() method in the descriptor means that
    # Python will use its default implementation of attribute lookup. This
    # requires that the supplied name matches the name used in the instance
    # dictionary.
    # If you comment out @shares(.setter) properties -> 
    #   AttributeError: 'PositiveInteger' object has no attribute '__get__'.

    # (d) Fixing the Names
    def __set_name__(self, cls, name):
        self.name = name

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

class PositiveInteger(Integer, Positive):
    ...

class PositiveFloat(Float, Positive):
    ...

class NonEmptyString(String, NonEmpty):
    ...


if __name__ == '__main__':
    assert hasattr(NonEmptyString, '__set__')
