# tableformat.py

from abc import ABC, abstractmethod

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()
    
    @abstractmethod
    def row(self, rowdat):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print(f'<tr> {"".join("<th>" + h + "</th>" for h in headers)} </tr>')
    
    def row(self, rowdata):
        print(f'<tr> {" ".join("<th>" + str(d) + "</th>" for d in rowdata)} </tr>')

# (b) Going Sideways
class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [fmt % d for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        headers = [h.upper() for h in headers]
        super().headings(headers)

# (c) Making it Sane
def create_formatter(fmt, column_formats=None, upper_headers=False):
    if fmt == 'txt':
        formatter_cls = TextTableFormatter
    elif fmt == 'csv':
        formatter_cls = CSVTableFormatter
    elif fmt == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % fmt)

    # Add Mixins
    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
            formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            ...

    return formatter_cls()

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, name) for name in fields]
        formatter.row(rowdata)


if __name__ == '__main__':
    import reader
    import stock
    portfolio = reader.read_csv_as_instances('../Data/portfolio.csv', stock.Stock)
    formatter = create_formatter('txt',
                                 column_formats=['%s', '%d', '%.2f'],
                                 upper_headers=True)
    print_table(portfolio, ['name', 'shares', 'price'], formatter)
