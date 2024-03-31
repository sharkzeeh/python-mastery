# readrides.py

import csv
from ridedata import RideData

def read_rides_as_fake_container(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            row[3] = int(row[3])
            records.append(dict(zip(headings, row)))
    return records

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

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes, dates, daytypes, numrides = [], [], [], []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()

    # rows
    # rows = read_rides_as_dictionaries('../Data/ctabus.csv')
    # print('Rows Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    # 203514872
    
    # columns
    # columns = read_rides_as_columns('../Data/ctabus.csv')
    # print('Columns Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    # # 96168404 - memory consumption is twice as low

    # fake container
    rows = read_rides_as_columns('../Data/ctabus.csv')
    print('Columns Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    # 96168404 - same as columned data
