# Handler Classes

# Sometimes code will implement a general 
# purpose algorithm, but will defer certain steps 
# to a separately supplied handler object

# Sometimes known as the "strategy" design pattern.

# The handler only contains the methods that 
# need to be implemented/customized

class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()
    
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
        print(','.join([str(d) for d in rowdata]))

# Builder
def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    else:
        raise RuntimeError('Unknown format %s' % fmt)

# Example of Handler class
def print_table(records, fields, formatter):
    '''
    formatter - handler class
    '''
    # call to handler method
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, name) for name in fields]
        # call to handler method
        formatter.row(rowdata)


if __name__ == '__main__':
    import reader
    import stock
    portfolio = reader.read_csv_as_instances('../Data/portfolio.csv', stock.Stock)
    formatter = TextTableFormatter()
    print_table(portfolio, ['name', 'shares'], formatter)