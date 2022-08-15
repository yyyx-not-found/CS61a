```python
>>> cats = [1, 2]
>>> dogs = [cats, cats.append(23), list(cats)]
>>> cats
[1, 2, 23]

>>> dogs[1] = list(dogs)
>>> dogs[1]
[[1, 2, 23], None, [1, 2, 23]]

>>> dogs[0].append(2)
>>> cats
[1, 2, 23, 2]

>>> cats[1::2]
[2, 2]

>>> cats[:3]
[1, 2, 23]

>>> dogs[2].extend([list(cats).pop(0), 3])
>>> dogs[3]
IndexError: list index out of range

>>> dogs
[[1, 2, 23, 2], [[1, 2, 23, 2], None, [1, 2, 23, 1, 3]], [1, 2, 23, 1, 3]]
```