# .close() method - terminates

import random

def producer():
    try:
        while True:
            yield random.random()
    except GeneratorExit:
        # .close() was invoked
        print('Producer generator has been closed.')
        return

def consumer(prod):
    for item in prod:
        if item < 0.7:
            yield item
        else:
            print('Closing the producer generator')
            prod.close()


if __name__ == '__main__':
    p = producer()
    c = consumer(p)
    for i in c:
        print(i)
    # 0.566772573711943
    # Closing the producer generator
    # Producer generator has been closed.
