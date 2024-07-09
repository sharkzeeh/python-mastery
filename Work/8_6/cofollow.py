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
        try:
            item = yield    # Receive an item sent to me
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)


if __name__ == '__main__':
    # follow('../Data/stocklog.csv', printer())
    ...