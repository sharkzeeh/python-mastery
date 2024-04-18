# (a) Closures as a data structure
def counter(value):
    def incr():
        nonlocal value
        value += 1
        return value

    def decr():
        value -= 1
        return value

    return incr, decr


if __name__ == '__main__':
    up, down = counter(0)
    print(up())
    print(up())
    print(down())
    print(down())
