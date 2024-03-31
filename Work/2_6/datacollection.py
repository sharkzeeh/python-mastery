# datacollection.py

from collections import abc

class DataCollection(abc.Sequence):
    def __init__(self, names):
        self.names = names
        for name in names:
            setattr(self, name, [])

    def __len__(self):
        return len(getattr(self, self.names[0]))  # Pick random column

    def __getitem__(self, index):
        d = {}
        for i, name in enumerate(self.names):
            d[name] = getattr(self, self.names[i])[index]
        return d

    def append(self, d):
        for i, k in enumerate(d):
            column = getattr(self, self.names[i])
            column.append(d[k])  # Store by reference
