# __del__ method

# Typical uses:
#   Proper shutdown of system resources (e.g., network connections)
#   Releasing locks (e.g., threading)
# Avoid defining it for any other purpose

class Connection:
    def __del__(self):
        # Cleanup
        ...
        print('Cleanup completed.')

if __name__ == '__main__':
    c = Connection()    # refcnt = 1
    d = c               # refcnt = 2
    del d               # Doesn't call d.__del__()  (refcnt = 1)
    c = None            # Calls c.__del__()         (refcnt = 0)
