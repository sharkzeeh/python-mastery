# (a) Slots vs. setattr

# In this example, there are no slots, but the __setattr__() method still restricts
# attributes to those in a predefined set. You'd probably need to
# think about how this approach might interact with inheritance (e.g., if subclasses wanted
# to add new attributes, they'd probably need to redefine __setattr__() to make it work).

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def __setattr__(self, name, value):
        if name not in { 'name', 'shares', 'price' }:
            raise AttributeError('No attribute %s' % name)
        super().__setattr__(name, value)    # default implementation


if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.1)
    try:
        s.share = 50
    except AttributeError as e:
        print(e)