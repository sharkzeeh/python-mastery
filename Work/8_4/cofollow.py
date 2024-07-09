# cofollow.py

import os
import time

# Data source
def follow(filename, target):
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if line:
                target.send(line)
            else:
                time.sleep(0.1)

# Decorator for coroutine functions
from functools import wraps
def consumer(func):
    @wraps(func)
    def start(*args, **kwargs):
        f = func(*args, **kwargs)
        f.send(None)    # Priming of the coroutine
        return f
    return start

# Sample coroutine
@consumer
def printer():
    while True:
        # (b) Raising Exceptions
        try:
            item = yield    # Receive an item sent to me
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)


# NOTE: the running generator is not terminated by the exception
# This is merely allowing the yield statement
#   to signal an error instead of receiving a value.
if __name__ == '__main__':
    # follow('../Data/stocklog.csv', printer())
    p = printer()
    p.send('hello')
    p.send(42)
    p.throw(ValueError('It failed'))
    try:
        int('N/A')
    except ValueError as e:
        p.throw(e)

    # hello
    # 42
    # ERROR: ValueError('It failed')
    # ERROR: ValueError("invalid literal for int() with base 10: 'N/A'")
