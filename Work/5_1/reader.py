# reader.py

import csv

def csv_as_dicts(lines, types, *, headers):
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
            record = { name: func(val) 
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records

def csv_as_instances(lines, cls, *, headers=None):
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types, *, headers=None):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers=headers)

def read_csv_as_instances(filename, cls, *, headers=None):
    '''
    Read CSV data into a list of instances
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers=headers)


if __name__ == '__main__':
    port = read_csv_as_dicts('../Data/portfolio.csv', [str, int, float])
    print(port)

    import stock
    port = read_csv_as_instances('../Data/portfolio.csv', stock.Stock)
    print(port)

    # (b) Thinking about Flexibility
    import gzip
    file = gzip.open('../Data/portfolio.csv.gz', 'rt')
    port = csv_as_instances(file, stock.Stock)
    print(port)

    # (c) Design Challenge: CSV Headers
    port = read_csv_as_instances(
        '../Data/portfolio_noheader.csv',
        stock.Stock,
        headers=False
    )
    print(port)
