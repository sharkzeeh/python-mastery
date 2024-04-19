# Descriptor Demo

# Whenever an attribute is accessed on a class,
# the attribute is checked to see if it is an 
# object that looks like a so-called "descriptor"

# A descriptor is an object with one or more of
# the following special methods
#   d.__get__(obj, cls)
#   d.__set__(obj, value)
#   d.__delete__(obj)

# If a descriptor is detected, one of the above
# methods gets triggered on access
# NOTE: __get__() can be omitted if the name
# exactly matches that in the instance dict

# Basically, a descriptor is just
# an object with __get__, __set__, and __delete__ methods

# Descriptors are presented with information
# about the instance, class, and values

# NOTE: `self` is the descriptor itself, 
#       `instance` is the object it's operating on
#       `cls` is the class of that instance (by default)

class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print('%s:__get__' % self.name)

    def __set__(self, instance, value):
        print('%s:__set__ %s' % (self.name, value))

    def __delete__(self, instance):
        print('%s:__delete__' % self.name)

# Descriptors are placed in class definitions
class Foo:
    a = Descriptor('a')
    b = Descriptor('b')


if __name__ == '__main__':
    f = Foo()
    f.a         # a:__get__
    f.a = 42    # a:__set__ 42
    del f.a     # a:__delete__

    x = f.b     # b:__get__
    print(x)    # None
    f.b = 42    # b:__set__ 42
    print(f.b)  # None
