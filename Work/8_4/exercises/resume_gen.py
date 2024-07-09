# In general, you can break out of running iteration
#   and resume it later if you need to.
# Just make sure the generator object
#   isn't forcefully closed or garbage collected somehow.

# follow.py

import os
import time

def follow(fname):
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
    # Experiment: Resuming a generator
    lines = follow('../Data/stocklog.csv')
    for line in lines:
        print(line, end='')
        if 'IBM' in line:
            print('IBM ticker found! Breaking out of while-loop immediately!')
            break

    # Resume iteration
    print('\nResuming the generator!\n')
    for line in lines:
        print(line, end='')
        if 'IBM' in line:
            print('IBM ticker found again! Closing the generator immediately!')
            break   # lines.close()
    del lines

    # "DIS",34.07,"6/11/2007","09:30.47",-0.13,34.28,34.07,34.04,118557
    # "T",39.90,"6/11/2007","09:30.47",-0.36,40.20,39.90,39.87,537322
    # "IBM",102.79,"6/11/2007","09:30.51",-0.28,102.87,102.79,102.77,87125
    # IBM ticker found! Breaking out of while-loop immediately!

    # Resuming the generator!

    # "MMM",85.72,"6/11/2007","09:30.51",-0.22,85.94,85.75,85.72,161998
    # "HPQ",45.63,"6/11/2007","09:30.52",-0.07,45.80,45.63,45.59,147403
    # "IBM",102.80,"6/11/2007","09:31.24",-0.27,102.87,102.80,102.77,95683
    # IBM ticker found again! Closing the generator immediately!
    # Following Done