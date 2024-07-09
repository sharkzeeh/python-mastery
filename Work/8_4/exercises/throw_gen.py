# .throw() method - raise an exception

def gen():
    while True:
        try:
            line = yield
            if 'insane' in line:
                print('This line is insane!')
        except RuntimeError as e:
            print(e)


if __name__ == '__main__':
    g = gen()
    g.send(None)
    g.send('sane')
    g.send('insane')
    g.throw(RuntimeError, "You're dead!")
    g.send('insane')
    # This line is insane!
    # You're dead!
    # This line is insane!
