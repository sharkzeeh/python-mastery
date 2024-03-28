# Consider a list of varying sized data structures
prices = [
    ['GOOG', 490.1, 485.25, 487.5 ],
    ['IBM', 91.5],
    ['HPE', 13.75, 12.1, 13.25, 14.2, 13.5 ],
    ['CAT', 52.5, 51.2]
]

for name, *values in prices:
    print(name, values)

# not `for name, values in ...`
# ValueError: too many values to unpack (expected 2)
