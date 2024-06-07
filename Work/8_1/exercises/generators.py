# (a) A Simple Generator

# 1. Generator function (exhaustive)
def frange(start, stop, step):
    while start < stop:
        yield start
        start += step

# 2. Generator class (non-exhaustive)
class FRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        n = self.start
        while n < self.stop:
            yield n
            n += self.step


if __name__ == '__main__':
    # 1. Generator function
    for x in frange(0, 2, 0.25):
        print(x, end=' ')
    print()

    f = frange(0, 2, 0.25)
    for x in f:
        print(x, end=' ')

    for x in f: # Nothing
        print(x, end=' ')

    # 2. Generator class
    f = FRange(0, 2, 0.25)
    for x in f:
        print(x, end=' ')
    
    for x in f: # Reusable generator
        print(x, end=' ')
    
    print()
    print(next(f.__iter__()))   # 0
    print(next(f.__iter__()))   # 0