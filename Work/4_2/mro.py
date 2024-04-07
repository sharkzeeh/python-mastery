#     object
#   /        \
#   A         B
#     \     /   \
#        C        D
#           \   /
#             E

class A:        pass
class B:        attr = 'B'
class C(A, B):  pass
class D(B):     attr = 'D'
class E(C, D):  pass


if __name__ == '__main__':
    e = E()
    print('E bases:', E.__bases__)  # C, D
    print(f'E mro:', E.__mro__)     # E, C, A, D, B -- Note: B goes last
    for cls in e.__class__.__mro__:
        if 'attr' in cls.__dict__:
            print(f'attr was found in class {cls.__name__}!')
            print('E.attr ==', E.attr)
            break
