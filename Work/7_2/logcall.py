# logcall.py

# (b) Your first decorator with arguments

from functools import wraps

def logformat(fmt):
    def logged(func):
        print('Adding logging to', func.__name__)
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return logged

# def logged(func):
#     print('Adding logging to', func.__name__)
#     def wrapper(*args, **kwargs):
#         print('Calling', func.__name__)
#         return func(*args, **kwargs)
#     return wrapper

# Write this instead of `logged` defition above
logged = logformat('Calling {func.__name__}')


if __name__ == '__main__':
    @logged
    def add(x, y):
        return x + y
    add(2, 3)

    @logformat('{func.__code__.co_filename}:{func.__name__}')
    def mul(x, y):
        return x * y
    mul(2, 3)
