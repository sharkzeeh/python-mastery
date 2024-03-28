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
            route, date, daytype, rides = row[0], row[1], row[2], int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides,
            }
            records.append(record)
    return records


if __name__ == '__main__':
    import pprint
    rows = read_rides_as_dictionaries('../Data/ctabus.csv')
    # 1. How many bus routes exist in Chicago?
    from collections import Counter
    routes_counter = Counter([row['route'] for row in rows])
    print(f'{len(routes_counter)} bus routes exist in Chicago')
    # 2. How many people rode the number 22 bus on February 2, 2011? What about any route on any date of your choosing?
    get_rides_number_on_date = lambda route, date: sum([row['rides'] for row in rows if row['date'] == date and row['route'] == route])
    print(get_rides_number_on_date('22', '02/02/2011'))
    # 3. What is the total number of rides taken on each bus route?
    pprint.pprint(routes_counter)
    # 4. What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
    timeframe = [row for row in rows 
                    if (dt := int(row['date'].split('/')[-1])) >= 2001 and 
                    dt <= 2011]
    select = [row['route'] for row in timeframe]
    routes_counter_framed = Counter(select).most_common(5)
    pprint.pprint(routes_counter_framed)
