# docstring in python

[Sphinx](https://www.sphinx-doc.org/)
[Pydoc](https://docs.python.org/3/library/pydoc.html)


Ways to get docstring of a function in Python:

- Get docstring of a function using attribute  
function_name.__doc__

- Using help() function to display docstring

- Using inspect module  
```python
import inspect
inspect.getdoc(function_name_here)
```



