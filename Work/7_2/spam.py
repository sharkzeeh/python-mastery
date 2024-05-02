# (c) Multiple decorators and methods

# Important to follow the order of the decorators
# with the implementation of decorator `logged`
# from section (a) or (b)

# def logged(func):
#     print('Adding logging to', func.__name__)
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Calling', func.__name__)
#         return func(*args, **kwargs)
#     return wrapper

from logcall import logged

class Spam:

    @logged
    def instance_method(self):
        pass

    @classmethod
    @logged
    def class_method(cls):
        pass

    @staticmethod
    @logged
    def static_method():
        pass

    @property
    @logged
    def property_method(self):
        pass


if __name__ == '__main__':
    s = Spam()
    s.instance_method()
    Spam.class_method()
    Spam.static_method()
    s.property_method
