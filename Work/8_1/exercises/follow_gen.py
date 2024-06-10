# follow.py
# (d) Monitoring a streaming data source

# Modify the code so that the file-reading is performed by
# a generator function follow(filename).
# Make it so the following code works:

import os
import time

def follow(fname):
    with open(fname) as fh:
        fh.seek(0, os.SEEK_END)     # Move file pointer 0 bytes from end of file
        while True:
            line = fh.readline()
            if not line:
                time.sleep(0.1)     # Sleep briefly and retry
                continue
            yield line


if __name__ == '__main__':
    for line in follow('../../Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print('%10s %10.2f %10.2f' % (name, price, change))

        # Example output
        # HPQ      45.68      -0.02
        # MSFT      29.98      -0.07
        # MRK      49.87      -0.27
        # GE      37.17      -0.15