import sys

# Notice how the size does not increase on every append
row = { 'route': '22', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354 }
print(sys.getsizeof(row))

row['a'] = 1
print(sys.getsizeof(row))
row['b'] = 2
print(sys.getsizeof(row))

del row['b']
print(sys.getsizeof(row))

# Food for thought: If you are creating large numbers of records,
# representing each record as a dictionary might not be the most
# efficient approach--you could be paying a heavy price for the convenience
# of having a dictionary. It might be better to consider the use of tuples,
# named tuples, or classes that define __slots__.
