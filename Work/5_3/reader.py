# reader.py

import csv

# (a) Using higher-order functions
# (b) Using map()
def convert_csv(lines, converter, *, headers=None):
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    return list(map(lambda row: converter(headers, row), rows))
    # for row in rows:
    #     record = converter(headers, row)
    #     records.append(record)
    # return records

def csv_as_dicts(lines, types, *, headers=None):
    def make_row(headers, row):
        return {
            name: func(val) for name, func, val in zip(headers, types, row)
        }
    return convert_csv(lines, make_row)

def csv_as_instances(lines, cls, *, headers=None):
    def make_row(headers, row):
        return cls.from_row(row)
    return convert_csv(lines, make_row)
    # return convert_csv(
    #     lines, 
    #     lambda headers, row: row: cls.from_row(row))

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
