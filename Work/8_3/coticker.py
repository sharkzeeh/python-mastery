# coticker.py
# (b) Build some pipeline components

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
import csv

# Coroutine that splits rows using the CSV module.
# This is rather mind-bending due to the fact that
# the csv module only understands iteration with the for-loop.
# To make it work, we wrap it around a generator
# that simply produces the last item received.
@consumer
def to_csv(target):
    def producer():
        while True:
            yield line
    reader = csv.reader(producer())
    while True:
        line = yield
        target.send(next(reader))

@consumer
def create_ticker(target):
    while True:
        row = yield
        target.send(Ticker.from_row(row))

@consumer
def negchange(target):
    while True:
        record = yield
        if record.change < 0:
            target.send(record)

@consumer
def ticker(fmt, fields):
    formatter = create_formatter(fmt)
    formatter.headings(fields)
    while True:
        rec = yield
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
