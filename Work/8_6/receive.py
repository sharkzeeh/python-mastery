# receive.py

# (a) Example: Receiving messages

from cofollow import consumer

# This function receives a message,
#     but then verifies that it is of an expected type
def receive(expected_type):
    msg = yield
    assert isinstance(msg, expected_type), 'Expected type %s' % (expected_type)
    return msg

# From a readability point of view,
# the yield from receive(int) statement is a bit more descriptive:
#   it indicates that the function will yield until
#   it receives a message of a given type.
@consumer
def print_ints():
    while True:
        msg = yield from receive(int)
        print('Got:', msg)


if __name__ == '__main__':
    p = print_ints()
    p.send(42)      # Got: 42
    p.send(13)      # Got: 13
    p.send('13')    # ERROR