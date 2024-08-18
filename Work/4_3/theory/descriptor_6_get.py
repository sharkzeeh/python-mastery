# Tricky Bits with __get__
# Descriptor Naming

class Descriptor:
    def __init__(self, name=None):
        self.name = name

    # Recommended __get__ implementation
    def __get__(self, instance, cls):
        # If no instance given, return the descriptor object itself
        if instance is None:
            print(self)                         # debug
            return self
        # Return the instance itself
        print(instance.__dict__[self.name])     # debug
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    # Allows to write x = Descriptor() -> x.__set_name__(Foo, 'x')
    # NOTE (how I see): descriptor needs at least one method
    #                   __init__ or __set_name__
    def __set_name__(self, cls, name):
        self.name = name

class Foo:
    # a = Descriptor('a')
    a = Descriptor()


if __name__ == '__main__':
    # __get__ can be accessed in two ways

    #   through an instance (bound)
    f = Foo()
    f.a = 42
    f.a      # 42

    #   on the class definition (unbound)
    Foo.a    # <__main__.Descriptor object at ...>

    # Always check for presence of an instance 
    # (instance). If None, return the descriptor itself
