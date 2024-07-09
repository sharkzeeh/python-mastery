# gensocket.py

# (b) Wrapping a Socket

class GenSocket:
    def __init__(self, sock):
        self.sock = sock

    def accept(self):
        yield 'recv', self.sock
        client, addr = self.sock.accept()
        return GenSocket(client), addr

    def recv(self, maxsize):
        yield 'recv', self.sock
        return self.sock.recv(maxsize)

    def send(self, data):
        yield 'send', self.sock
        return self.sock.send(data)

    # allows to use sock.listen(5), self.bind(address), etc.
    def __getattr__(self, name):
        return getattr(self.sock, name)
    
    # TODO: Implement context manager
    def __enter__(self, *args, **kwargs):
        return self.sock.__enter__(*args, **kwargs)

    def __exit__(self, *args, **kwargs):
        self.sock.close()
