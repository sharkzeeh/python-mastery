# follow.py

import os
import time

def follow(fname):
    # (a) Closing a Generator
    try:
        with open(fname) as fh:
            fh.seek(0, os.SEEK_END)     # Move file pointer 0 bytes from end of file
            while True:
                line = fh.readline()
                if not line:
                    time.sleep(0.1)     # Sleep briefly and retry
                    continue
                yield line
    except GeneratorExit:
        print('Following Done')


if __name__ == '__main__':
    # (a) Closing a Generator
    # Experiment: Garbage collection of a running generator
    lines = follow('../Data/stocklog.csv')
    print(next(lines))
    print(next(lines))
    # NOTE: `del lines` is optional in file execution, but in interactive mode
    # you would need to stop the generator by yourself
    del lines
    # "MRK",50.21,"6/11/2007","09:35.57",0.07,50.30,50.21,49.66,1451639
    # "PG",62.83,"6/11/2007","09:35.59",-0.24,62.80,62.83,62.61,290465
    # Following Done

    # Experiment: Closing a generator
    lines = follow('../Data/stocklog.csv')
    for line in lines:
        print(line, end='')
        if 'IBM' in line:
            print('IBM ticker found! Closing immediately!')
            lines.close()

    for line in lines:
        print(line, end='')     # No output: generator is done
    # "MRK",50.25,"6/11/2007","09:36.23",0.11,50.30,50.25,49.66,1466026
    # "IBM",102.89,"6/11/2007","09:36.24",-0.18,102.87,102.89,102.77,173483
    # IBM ticker found! Closing immediately!
    # Following Done
