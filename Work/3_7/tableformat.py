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

def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError('Unknown format %s' % fmt)

# (a) Interfaces and type checking
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

    # (a) Interfaces and type checking
    class MyFormatter:
        def headings(self, headers): ...
        def row(self, rowdata): ...
    wrong_formatter = MyFormatter()
    try:
        print_table(portfolio, ['name','shares', 'price'], wrong_formatter)
    except TypeError as e:
        print(e)

    formatter = create_formatter('txt')
    print_table(portfolio, ['name','shares', 'price'], formatter)
