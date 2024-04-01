# Weak References

# A weak reference is a reference to an object 
# that does not increase its reference count

# Sometimes this is desired in when there is a 
# complicated relationship between objects and 
# there are issues with memory management

# Weak references are sometimes used where 
# there are reference cycles between objects
# Example : graphs, trees, observers, caches,etc.
# Not something you should consider unless 
# dealing with really tricky memory problems

class Foo:
    pass


if __name__ == '__main__':
    import weakref
    f = Foo()
    fref = weakref.ref(f)
    print('fref:', fref)

    # get the object being pointed at
    g = fref()  # Dereference
    print('g:', g)
    assert g == f

    # if the object is dead, dereference returns None
    del f, g
    print('fref():', fref())
