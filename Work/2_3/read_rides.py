# readrides.py

import csv

def read_rides_as_dictionaries(filename):
    '''
    Read the bus ride data as a list of dictionaries
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            record = dict(zip(headings, row))
            records.append(record)
    return records

def read_rides_as_generator(filename):
    '''
    Read the bus ride data as a list of dictionaries
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        records = (dict(zip(headings, row)) for row in rows)
        for record in records:
            yield record
        # PROBLEM:
        # the file will be closed
        # only after the generator is exhausted
    # !!! return records - https://stackoverflow.com/questions/39656437/


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    # # 1. list of dictionaries
    # rows = read_rides_as_dictionaries('../Data/ctabus.csv')
    # rt22 = [row for row in rows if row['route'] == '22']
    # max_date = max(rt22, key=lambda row: int(row['rides']))
    # print(max_date)
    # print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())

    # 2. generator
    rows = read_rides_as_generator('../Data/ctabus.csv')
    rt22 = (row for row in rows if row['route'] == '22')
    max_date = max(rt22, key=lambda row: int(row['rides']))
    print(max_date)
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    