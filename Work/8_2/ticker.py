# ticker.py
# (b) Making more pipeline components
# (c) Keep going

from structure import Structure

class Ticker(Structure):
    name = String()     # type: ignore
    price = Float()     # type: ignore
    date = String()     # type: ignore
    time = String()     # type: ignore
    change = Float()    # type: ignore
    open = Float()      # type: ignore
    high = Float()      # type: ignore
    low = Float()       # type: ignore
    volume = Integer()  # type: ignore


if __name__ == '__main__':
    from follow import follow
    import csv
    lines = follow('../Data/stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)

    # (b) Making more pipeline components
    # for record in records:
    #     print(record)
    # Ticker('DD', 51.14, '6/11/2007', '09:57.21', 0.01, 51.13, 51.18, 50.6, 365548)
    # Ticker('IBM', 103.57, '6/11/2007', '09:57.24', 0.5, 102.87, 103.6, 102.77, 580371)
    # Ticker('AA', 39.95, '6/11/2007', '09:57.31', 0.29, 39.67, 40.15, 39.31, 629412)

    # (c) Keep going
    from tableformat import create_formatter, print_table
    formatter = create_formatter('text')
    negative = (rec for rec in records if rec.change < 0)
    print_table(negative, ['name', 'price', 'change'], formatter)
    #       name      price     change
    # ---------- ---------- ---------- 
    #         GE      37.26      -0.06
    #         JPM     50.38      -0.03
    #         UTX     69.84      -0.39

# Discussion

# Some lessons learned: You can create various generator functions and
# chain them together to perform processing involving data-flow
# pipelines.

# A good mental model for generator functions might be Lego blocks.
# You can make a collection of small iterator patterns and start
# stacking them together in various ways. It can be an extremely powerful way to program.
