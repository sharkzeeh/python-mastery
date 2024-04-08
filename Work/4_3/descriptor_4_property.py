# Descriptors and Properties
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
    print(p)
    p.__set__(s, 100)    # Same as s.shares = 100
    p.__get__(s, Stock)  # Same as s.shares
    s.shares
