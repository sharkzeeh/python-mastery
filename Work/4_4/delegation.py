# (c) Delegation as an alternative to inheritance
# Delegation is sometimes used as an alternative to inheritance.
# The idea is almost the same as the proxy class
# you defined in part (b). Try defining the following class:

class Spam:
    def a(self):
        print('Spam.a')
    def b(self):
        print('Spam.b')

class MySpam:
    def __init__(self):
        self._spam = Spam()
    def a(self):
        print('MySpam.a')
        self._spam.a()
    def c(self):
        print('MySpam.c')
    def __getattr__(self, name):
        return getattr(self._spam, name)    # s.b()


if __name__ == '__main__':
    s = MySpam()
    s.a()
        # MySpam.a
        # Spam.a
    s.b()
        # Spam.b
    s.c()
        # MySpam.c
