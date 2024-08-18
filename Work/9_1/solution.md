## (c) from module import

```python
>>> from simplemod import x, foo
>>> x
42
>>> foo()
x is 42
>>> x = 13
>>> foo()
x is 42                   # !! Please explain
>>> x
13
>>>
```

## Explain
`x` is still 42, because the value of `x` in the function `simplemod.foo` was read from module `simplemod.x`
