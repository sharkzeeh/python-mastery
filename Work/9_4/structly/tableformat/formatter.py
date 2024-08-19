# tableformat/formatter.py

# (b) Subclass Registration
# (c) Dynamic Imports

from abc import ABC, abstractmethod

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise RuntimeError('Expected a TableFormatter')

    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

class TableFormatter(ABC):
    ### (b) Subclass Registration
    _formats = {}

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls
    ###

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

# from .formats.text import TextTableFormatter
# from .formats.csv import CSVTableFormatter
# from .formats.html import HTMLTableFormatter

class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [ (fmt % item) for fmt, item in zip(self.formats, rowdata)]
        super().row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])

def create_formatter(name, column_formats=None, upper_headers=False):

    ### (b) Subclass Registration
    ### (c) Dynamic Imports
    if name not in TableFormatter._formats:
        # print(__package__)    # structly.tableformat
        __import__(f'{__package__}.formats.{name}')

    formatter_cls = TableFormatter._formats.get(name)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % name)
    ###

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
