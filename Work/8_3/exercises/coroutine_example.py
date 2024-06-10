# Example from PDF 8-20 -- 8-28

import os
import time

# A source that mimics Unix 'tail -f'
def follow(filename,target):
    with open(filename, 'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line:
                target.send(line)
            else:
                time.sleep(0.1)

# Prime the coroutine
def consumer(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.send(None)
        return cr
    return start

# A consumer that just prints the lines
@consumer
def printer():
    while True:
        line = yield
        print(line, end=' ')

# A filter coroutine
@consumer
def match(pattern, target):
    while True:
        line = yield            # Receive a line
        if pattern in line:
            target.send(line)   # Send to next stage


if __name__ == '__main__':
    follow('../../Data/stocklog.csv', match('IBM', printer()))
    # "IBM",102.78,"6/11/2007","09:30.17",-0.29,102.87,102.78,102.77,78308
    #  "IBM",102.79,"6/11/2007","09:30.51",-0.28,102.87,102.79,102.77,87125

# follow() ---send()--> match() ---send()--> printer()
