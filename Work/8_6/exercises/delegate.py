def countdown(n):
    while n > 0:
        yield n
        n -= 1

def countup(end):
    n = 0
    while n < end:
        yield n
        n += 1
    return n    # generators can also return a value (last yield)

# Option 1: Drive the generator yourself
def up_and_down_1(n):
    for x in countup(n):
        yield x
    for x in countdown(n):
        yield x

# Option 2: Let Python drive the generator (yield from)
# Whatever "outer" code runs
# the generator will take care of it (you don't worry about it)
def up_and_down_2(n):
    res = yield from countup(n)
    assert res == n     # True
    yield from countdown(n)


if __name__ == '__main__':
    for i in up_and_down_2(5):
        print(i)
