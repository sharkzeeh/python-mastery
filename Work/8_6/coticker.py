# coticker.py

# (a) Example: Receiving messages

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

from cofollow import consumer, follow
from tableformat import create_formatter
from receive import receive
import csv

@consumer
def to_csv(target):
    def producer():
        while True:
            yield line
    reader = csv.reader(producer())
    while True:
        # (a) Example: Receiving messages
        line = yield from receive(str)
        target.send(next(reader))

@consumer
def create_ticker(target):
    while True:
        # (a) Example: Receiving messages
        row = yield from receive(list)
        target.send(Ticker.from_row(row))

@consumer
def negchange(target):
    while True:
        # (a) Example: Receiving messages
        record = yield from receive(Ticker)
        if record.change < 0:
            target.send(record)

@consumer
def ticker(fmt, fields):
    formatter = create_formatter(fmt)
    formatter.headings(fields)
    while True:
        # (a) Example: Receiving messages
        rec = yield from receive(Ticker)
        row = [getattr(rec, name) for name in fields]
        formatter.row(row)


if __name__ == '__main__':
    follow(
        '../Data/stocklog.csv',
        to_csv(
            create_ticker(
                negchange(
                    ticker('text',  ['name', 'date', 'change'])
                )
            )
        )
    )
    # ---------- ---------- ----------
    #       name       date     change
    #          C  6/11/2007      -0.34
    #        AIG  6/11/2007      -0.24
    #         VZ  6/11/2007      -0.03

    # NOTE: to show all attributes use
    #   ticker('text', Ticker._fields)
