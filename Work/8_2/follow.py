# follow.py
# (a) Setting up a processing pipeline

import os
import time

def follow(fname):
    with open(fname) as fh:
        fh.seek(0, os.SEEK_END) # Move file pointer 0 bytes from end of file
        while True:
            line = fh.readline()
            if not line:
                time.sleep(0.1)   # Sleep briefly and retry
                continue
            yield line


if __name__ == '__main__':
    import csv
    lines = follow('../Data/stocklog.csv')
    rows = csv.reader(lines)
    for row in rows:
        print(row)
    # ['VZ', '42.79', '6/11/2007', '09:30.11', '-0.28', '42.95', '42.79', '42.78', '123028']
    # ['DD', '50.61', '6/11/2007', '09:30.13', '-0.52', '51.13', '50.61', '50.60', '12897']
    # ['MRK', '49.68', '6/11/2007', '09:30.13', '-0.46', '50.30', '49.68', '49.66', '1261293']

# What you're seeing here is that the output of the follow() function
# has been piped into the csv.reader() function and we're
# now getting a sequence of split rows.
