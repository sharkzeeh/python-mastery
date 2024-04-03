from abc import ABC, abstractmethod

class IStream(ABC):
    @abstractmethod
    def read(self, maxbytes=None):
        pass
    @abstractmethod
    def write(self, data):
        pass

# UnixPipe class must implement all abstract methods
# otherwise it can't be instantiated
class UnixPipe(IStream):
    def read(self, maxbytes=None):
        ...
    def write(self, data):
        ...


if __name__ == '__main__':
    p = UnixPipe()
    p.write('data')
