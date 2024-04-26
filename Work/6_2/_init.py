# (a) Show me your locals
# def _init(locs):
#     self = locs.pop('self')
#     for name, val in locs.items():
#         setattr(self, name, val)

# (b) Frame Hacking
import sys
def _init():
    locs = sys._getframe(1).f_locals    # Get callers local variables
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)

class Stock:
    def __init__(self, name, shares, price):
        # (a) Show me your locals
        # print(locals())
        # {
        #     'self': <__main__.Stock object at 0x100699b00>,
        #     'price': 490.1, 'name':
        #     'GOOG', 'shares': 100
        # }
        # _init(locals())

        # (b) Frame Hacking
        _init()


if __name__ == '__main__':
    s = Stock(name='GOOG', price=490.1, shares=50)
    print(s.name, s.shares, s.price)