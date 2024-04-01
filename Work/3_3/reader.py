# reader.py

import csv
import stock
import bus_row

def read_csv_as_instances(fname, cls):
    records = []
    with open(fname) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records


if __name__ == '__main__':
    portfolio = read_csv_as_instances('../Data/portfolio.csv', stock.Stock)
    print(portfolio)

    # different data and class
    rides = read_csv_as_instances('../Data/ctabus.csv', bus_row.Row)
    print(len(rides))
