class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(selF):
        print('B.spam')
        super().spam()

class C(B):
    def spam(self):
        print('C.spam')
        super().spam()


if __name__ == '__main__':
    c = C()
    c.spam()
    # C.spam
    # B.spam
    # A.spam
