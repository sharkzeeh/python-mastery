# `import` statement

```python
# foo.py

def grok(a):
    ...

def spam(b):
    ...
```

```python
import sys
import foo

foo.grok(2) # dummy

current_module_dict = sys.modules[__name__].__dict__

if 'foo' in current_module_dict:    # module `foo` is cached
    print(current_module_dict['foo'])   # <module 'foo' from ...
```

# `from module import ...`

Selected symbols can be imported locally

## Confusion
This does not change how import works. The entire module executes and is cached. This merely copies a name.

```python
import sys
from foo import grok    # module `foo` was fully cached

print(sys.modules['foo'])   # <module 'foo' from ...
```

# Module Cache
* Each module is loaded ***only once***
* Repeated imports just return a *reference* to the *previously loaded module*
* `sys.modules` is a dict of all loaded modules
```python
>>> import sys
>>> list(sys.modules)
['copy_reg', '__main__', 'site', '__builtin__',
'encodings', 'encodings.encodings', 'posixpath', ...]
```
