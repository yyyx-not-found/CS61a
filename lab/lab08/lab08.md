```python
---------------------------------------------------------------------
Iterators > Suite 1 > Case 1

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> s = [1, 2, 3, 4]
>>> t = iter(s)
>>> next(s)
? Error

>>> next(t)
? 1

>>> next(t)
? 2

>>> iter(s)
? Iterator

>>> next(iter(s))
? 1

>>> next(iter(t))
? 3

>>> next(iter(s))
? 1

>>> next(iter(t))
? 4

>>> next(t)
? StopIteration

---------------------------------------------------------------------
Iterators > Suite 1 > Case 2
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> r = range(6)
>>> r_iter = iter(r)
>>> next(r_iter)
? 0

>>> [x + 1 for x in r]
? [1, 2, 3, 4, 5, 6]

>>> [x + 1 for x in r_iter]
? [2, 3, 4, 5, 6]

>>> next(r_iter)
? StopIteration

>>> list(range(-2, 4))   # Converts an iterable into a list
? [-2, -1, 0, 1, 2, 3]

---------------------------------------------------------------------
Iterators > Suite 1 > Case 3
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> map_iter = map(lambda x : x + 10, range(5))
>>> next(map_iter)
? 10

>>> next(map_iter)
? 11

>>> list(map_iter)
? [12, 13, 14]

>>> for e in filter(lambda x : x % 2 == 0, range(1000, 1008)):
...     print(e)
(line 1)? 1000
(line 2)? 1002
(line 3)? 1004
(line 4)? 1006

>>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
? [5, 7, 9]

>>> for e in zip([10, 9, 8], range(3)):
...   print(tuple(map(lambda x: x + 2, e)))
(line 1)? (12, 2)
(line 2)? (11, 3)
(line 3)? (10, 4)

---------------------------------------------------------------------
```