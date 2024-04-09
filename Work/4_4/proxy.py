# (b) Proxies
# A proxy class is a class that wraps around an existing class
# and provides a similar interface.

# Define the following class which makes a read-only layer
# around an existing object
class Readonly:
    def __init__(self, obj):
        self.__dict__['_obj'] = obj
        # NOTE: can't use self._obj = obj here
    def __setattr__(self, name, value):
        raise AttributeError("Can't set attribute")
    def __getattr__(self, name):
        return getattr(self._obj, name)


if __name__ == '__main__':
    from stock import Stock
    s = Stock('GOOG', 100, 490.1)
    ros = Readonly(s)
    print(ros.name, ros.shares, ros.cost)
    try:
        ros.shares = 50
    except AttributeError as e:
        print(e)
    # ros.__dict__['shares'] = 42   # still works
