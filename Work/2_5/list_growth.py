import sys

# Notice how the size does not increase on every append
items = []
print('List size after each iteration:')
size = sys.getsizeof(items)
print(size)
for i in range(5):
    items.append(i)
    size = sys.getsizeof(items)
    print('\t', i, ':', size)
