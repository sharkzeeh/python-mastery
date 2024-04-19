# Descriptors and Properties

# A property is also a descriptor

class Stock:
    @property
    def shares(self):
        print(self._shares)  # debug
        return self._shares
    @shares.setter
    def shares(self, value):
        self._shares = value


if __name__ == '__main__':
    s = Stock()
    p = Stock.__dict__['shares']
    print(p)                # <property object at ...>
    p.__set__(s, 100)       # same as s.shares = 100
    p.__get__(s, Stock)     # same as s.shares
    s.shares
