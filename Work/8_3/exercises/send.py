def gen():
    while True:
        line = yield 1, 2
        line = 3
        yield line

g = gen()
x, y = g.send(None)
print(x, y)     # 1, 2

z = g.send(None)
print(z)        # 3
