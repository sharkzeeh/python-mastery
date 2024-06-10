# cofollow.py
# (a) A coroutine example

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
        item = yield    # Receive an item sent to me
        print(item)


if __name__ == '__main__':
    follow('../Data/stocklog.csv', printer())
    # "CAT",78.00,"6/11/2007","09:30.06",-0.52,78.32,78.00,77.99,170217
    # "MRK",49.67,"6/11/2007","09:30.07",-0.47,50.30,49.67,49.66,1257973
    # "JNJ",62.09,"6/11/2007","09:30.09",-0.04,62.89,62.09,62.08,256102
