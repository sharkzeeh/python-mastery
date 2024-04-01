import time

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Sometimes you might use __new__() directly
    @classmethod
    def today(cls):
        t = time.localtime()
        self = cls.__new__(cls)
        self.year = t.tm_year
        self.month = t.tm_mon
        self.day = t.tm_mday
        return self


if __name__ == '__main__':
    d1 = Date(2012, 12, 21)
    d2 = Date.__new__(Date, 2012, 12, 21)
    print('d1:', d1)
    print('d2:', d2)

    # Creates an instance, but bypasses __init__()
    d3 = Date.today()  # uses __new__
    print('d3:', d3)
