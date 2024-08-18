# Locating Modules

* When looking for modules, Python first looks in the same directory as the source file that's executing the import

* If a module can't be found there, an internal module search path is consulted

```python
>>> import sys
>>> print(sys.path)
['',
 '/usr/local/lib/python36.zip',
 '/usr/local/lib/python3.6',
 '/usr/local/lib/python3.6/plat-darwin',
 '/usr/local/lib/python3.6/lib-dynload',
 '/usr/local/lib/python3.6/site-packages']
```

# Module Search Path
* `sys.path` contains search path
* Can manually adjust if you need to
```python
>>> import sys
>>> sys.path.append('/project/foo/pyfiles')
```
* Paths also added via environment variables
```sh
% env PYTHONPATH=/project/foo/pyfiles python3
Python 3.6.0 (default, Jan 12 2017, 13:20:23)
[GCC 4.2.1 Compatible Apple LLVM 6.1.0 (clang-602.0.53)]
```
```python
>>> import sys
>>> sys.path
['', '/project/foo/pyfiles',
 '/usr/local/lib/python36.zip', ... ]
 ```
