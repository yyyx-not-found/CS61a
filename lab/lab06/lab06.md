```python
---------------------------------------------------------------------
List Mutation > Suite 1 > Case 1

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> lst = [5, 6, 7, 8]
>>> lst.append(6)
? Nothing

>>> lst
? [5, 6, 7, 8, 6]

>>> lst.insert(0, 9)
>>> lst
? [9, 5, 6, 7, 8, 6]

>>> x = lst.pop(2)
>>> lst
? [9, 5, 7, 8, 6]

>>> lst.remove(x)
>>> lst
? [9, 5, 7, 8]

>>> a, b = lst, lst[:]
>>> a is lst
? True

>>> b == lst
? True

>>> b is lst
? False

---------------------------------------------------------------------
```