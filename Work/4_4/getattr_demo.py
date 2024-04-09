# __getattr__
# The __getattr__() method is commonly defined on classes that act as
# wrappers around other objects. However, you have to be aware that the
# process of wrapping another object in this manner often introduces
# other complexities. For example, the wrapper object might break
# type-checking if any other part of the application is using the
# isinstance() function.

# Delegating methods through __getattr__() also doesn't work with special
# methods such as __getitem__(), __enter__(), and so forth. If a class
# makes extensive use of such methods, you'll have to provide similar functions
# in your wrapper class.

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

# Proxy
# It holds an internal reference to an object
# Attribute access is redirected to held object
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # A failsafe method. Called if an attribute can't 
    # be found using the standard mechanism
    # __getattr__  doesn't apply to special methods 
    # (e.g., __len__,  __getitem__ , etc.)
    def __getattr__(self, name):
        print('geattr:', name)
        return getattr(self._obj, name)


if __name__ == '__main__':
    c = Circle(4.0)
    print(c.radius)
    print(c.area())
    p = Proxy(c)
    print(p.radius)
    print(p.area())
