# reader.py

import csv
from datacollection import DataCollection

# (b) Making a Parsing Utility Function
def read_csv_as_dicts(fname, types):
    records = []
    with open(fname) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = {colname: func(val) 
                      for colname, func, val 
                      in zip(headings, types, row)}
            records.append(record)
    return records

# (d) Special Challenge Project
def read_csv_as_columns(fname):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    records = None
    with open(fname) as f:
        rows = csv.reader(f)
        headings = next(rows)
        records = DataCollection(headings)
        for row in rows:
            records.append(dict(zip(headings, row)))
    return records

if __name__ == '__main__':
    # (c) Memory Revisited
    import tracemalloc
    tracemalloc.start()

    # data = read_csv_as_dicts('../Data/ctabus.csv', [str, str, str, int])
    # print(len(data))
    # print(data[0])
    # print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    # 188373117

    from sys import intern
    data = read_csv_as_columns('../Data/ctabus.csv', [intern, intern, str, int])
    print(len(data))
    print(data[0])
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    # 111315200