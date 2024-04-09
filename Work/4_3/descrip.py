# descrip.py

class Descriptor:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, cls):
        print('%s:__get__' % self.name)
    def __set__(self, instance, value):
        print('%s:__set__ %s' % (self.name, value))
    def __delete__(self, instance):
        print('%s:__delete__' % self.name)

class Foo:
        a = Descriptor('a')
        b = Descriptor('b')
        c = Descriptor('c')

if __name__ == '__main__':
    f = Foo()
    f.a         # a:__get__
    f.b         # b:__get__
    f.a = 23    # a:__set__ 23
    del f.a     # a:__delete__
    # You have captured the dot-operator
    # for a specific attribute.
