# readrides.py

import csv
import typing

# Tuple
def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route, date, daytype, rides = row[0], row[1], row[2], int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

# Dictionary
def read_rides_as_dictionaries(filename):
    '''
    Read the bus ride data as a list of dictionaries
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route, date, daytype, rides = row[0], row[1], row[2], int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides,
            }
            records.append(record)
    return records

# Named tuple
class RowNamedTuple(typing.NamedTuple):
    route: str
    date: str
    daytype: str
    rides: int

def read_rides_as_namedtuples(filename):
    '''
    Read the bus ride data as a list of named tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route, date, daytype, rides = row[0], row[1], row[2], int(row[3])
            record = RowNamedTuple(route, date, daytype, rides)
            records.append(record)
    return records

# Class
class RowClass:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_classes(filename):
    '''
    Read the bus ride data as a list of classes
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route, date, daytype, rides = row[0], row[1], row[2], int(row[3])
            record = RowClass(route, date, daytype, rides)
            records.append(record)
    return records

# Class with __slots__
class RowClassWithSlots:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_classes_with_slots(filename):
    '''
    Read the bus ride data as a list of classes
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route, date, daytype, rides = row[0], row[1], row[2], int(row[3])
            record = RowClassWithSlots(route, date, daytype, rides)
            records.append(record)
    return records


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    # # 1. Tuples
    # rows = read_rides_as_tuples('../Data/ctabus.csv')
    # print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())

    # # 2. Dictionaries
    # rows = read_rides_as_dictionaries('../Data/ctabus.csv')
    # print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())

    # # 3. Named tuples
    # rows = read_rides_as_namedtuples('../Data/ctabus.csv')
    # print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())

    # # 4. Classes
    # rows = read_rides_as_classes('../Data/ctabus.csv')
    # print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())

    # 5. Classes with slots
    rows = read_rides_as_classes_with_slots('../Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
