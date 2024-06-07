# follow.py
# (d) Monitoring a streaming data source

import os
import time

f = open('../../Data/stocklog.csv')
f.seek(0, os.SEEK_END)  # Move file pointer 0 bytes from end of file

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # Sleep briefly and retry
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))

# NOTE: The use of the readline() method in this example is
# somewhat unusual in that it is not the usual way of reading lines from
# a file (normally you would just use a for-loop).
# However, in this case, we are using it to
# repeatedly probe the end of the file to see if more data has been added:
# readline() will either return new data or an empty string.
