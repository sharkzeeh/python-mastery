# (a) Experiment with exec()

code = '''
for i in range(n):
    print(i, end=' ')
print()
'''

n = 10
exec(code)

#
class Stock:
    _fields = ('name', 'shares', 'price')

argstr = ','.join(Stock._fields)
code = f'def __init__(self, {argstr}):\n'
for name in Stock._fields:
    code += f'  self.{name} = {name}\n'
print(code)

# In this example, an __init__() function is made directly from the _fields variable.
# There are no weird hacks involving a special _init() method or stack frames.
locs = {}
exec(code, locs)

## same as ?
locs = locals()
exec(code, globals(), locs)
# or just `exec(code, locs)``

Stock.__init__ = locs['__init__']
s = Stock('GOOG', 100, 490.1)
print(s.__dict__)
