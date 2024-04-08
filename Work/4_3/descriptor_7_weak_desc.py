# Weaker descriptors that only have __get__
# __get__ only triggered if obj.__dict__ doesn't match

# P.S. compare with descriptor_2_binding.py
#       where the descriptor runs regardless
#       the value in the instance dictionary

class MethodDescriptor:
    def __get__(self, instance, cls):
        print('Getting!')

class Foo:
    a = MethodDescriptor()

if __name__ == '__main__':
    f = Foo()
    f.a                     # Getting!
    f.__dict__['a'] = 42
    print(f.a)              # 42

    # NOTE: the value in the dictionary hides the descriptor
