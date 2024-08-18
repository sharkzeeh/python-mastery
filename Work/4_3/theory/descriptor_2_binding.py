# Descriptor Binding

# Descriptors always override __dict__

class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls=None):
        print(f'{self.name}:__get__')
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class Foo:
    a = Descriptor('a')
    b = Descriptor('b')


if __name__ == '__main__':
    # f = Foo()
    # f.a = 23            # stores value in f.__dict__['a']
    f = Foo()
    f.__dict__['a'] = 42
    print('f.__dict__:', f.__dict__)    # {'a': 42}
    value = f.a                         # a:__get__
    print(value)                        # 42

    # The descriptor runs regardless
    # The value in the instance dictionary
    # NOTE: different behaviour of descriptors
    #       that only implement __get__ method
    #       (see descriptor_6_get.py)
