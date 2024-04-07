class Base:
    def spam(self):
        print('Base.spam')
    
class X(Base):
    def spam(self):
        print('X.spam')
        super().spam()

class Y(Base):
    def spam(self):
        print('Y.spam')
        super().spam()

class Z(Base):
    def spam(self):
        print('Z.spam')
        super().spam()

class M(X, Y, Z):
    ...


if __name__ == '__main__':
    print(M.__mro__)
    m = M()
    m.spam()
    # X.spam
    # Y.spam
    # Z.spam
    # Base.spam

    # super() moves to the next class in the MRO
    # the exact order is controlled by the child
