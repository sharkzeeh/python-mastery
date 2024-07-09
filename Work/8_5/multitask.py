# multitask.py

# (a) Generators as tasks

from collections import deque

tasks = deque()

# Manager
def run():
    while tasks:
        task = tasks.popleft()      # Get a task
        try:
            task.send(None)         # Run to yield
            tasks.append(task)      # Reschedule
        except StopIteration:
            print('Task done')

# Task 1
def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield                       # bare yield
        n -= 1

# Task 2
def countup(n):
    x = 0
    while x < n:
        print('Up we go', x)
        yield                       # bare yield
        x += 1

    
# NOTE: task.send(None) will run the task code UNTIL the next yield.
# It means that only after second iteration of the cycle
# the values of `x` or `n` will get updated
# We see tasks cycling, but there are no threads
if __name__ == '__main__':
    tasks.append(countdown(10))
    tasks.append(countdown(5))
    tasks.append(countup(20))
    run()

    # T-minus 10
    # T-minus 5
    # Up we go 0
    # T-minus 9
    # T-minus 4
    # Up we go 1
    # T-minus 8
    # T-minus 3
    # Up we go 2
    # T-minus 7
    # T-minus 2
    # Up we go 3
    # T-minus 6
    # T-minus 1
    # Up we go 4
    # T-minus 5
    # Task done
    # Up we go 5
    # T-minus 4
    # Up we go 6
    # T-minus 3
    # Up we go 7
    # T-minus 2
    # Up we go 8
    # T-minus 1
    # Up we go 9
    # Task done
    # Up we go 10
    # Up we go 11
    # Up we go 12
    # Up we go 13
    # Up we go 14
    # Up we go 15
    # Up we go 16
    # Up we go 17
    # Up we go 18
    # Up we go 19
    # Task done