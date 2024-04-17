import time
import threading

def worker(x, y):
    print('About to work')
    time.sleep(5)
    print('Done')
    return x + y


if __name__ == '__main__':
    res = worker(2, 3)
    print(res)  # prints 5

    t = threading.Thread(target=worker, args=(2, 3))
    t.start()   # does not print the result

    # Carefully notice that the result of the calculation appears nowhere. Not only that, you don't even
    # know when it's going to be completed. There is a certain coordination problem here.
    # The convention for handling this case is to wrap the result of a function
    # in a Future. A Future represents a future result (see ./futures_2.py)
