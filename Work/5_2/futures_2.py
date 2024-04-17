import time
import threading
from concurrent.futures import Future

def worker(x, y):
    print('About to work')
    time.sleep(5)
    print('Done')
    return x + y

def do_work(x, y, fut):
    fut.set_result(worker(x, y))

if __name__ == '__main__':
    fut = Future()
    t = threading.Thread(target=do_work, args=(2, 3, fut))
    t.start()
    res = fut.result()
    print(res)  # prints 5
