# reader.py

import csv

def convert_csv(lines, converter, *, headers=None):
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    records = []
    for i, row in enumerate(rows, start=1):
        try:
            record = converter(headers, row)
            records.append(record)
        except ValueError as e:
            print(f'Row {i}: Bad row: {row}')
            log.warning(f'Row {i}: Reason: {e}')
    return records

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
