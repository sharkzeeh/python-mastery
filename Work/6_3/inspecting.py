def add(x, y):
    'Adds two things'
    x + y

if __name__ == '__main__':
    # (a) Inspecting functions
    print('dir(add):', dir(add))

    # (b) Using the inspect module
    import inspect
    sig = inspect.signature(add)
    print(repr(sig))        # <Signature (x, y)>
    print(sig.parameters)   # OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">)])
    print(tuple(sig.parameters))    # ('x', 'y')
