# Q1
```python
Recursion > Suite 1 > Case 1

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def f(a, b):
...     if a > b:
...         return f(a - 3, 2 * b)
...     elif a < b:
...         return f(b // 2, a)
...     else:
...         return b
>>> f(2, 2)
? 2

>>> f(7, 4)
? 4

>>> f(2, 28)
? 8

>>> f(-1, -3)
? Infinite

---------------------------------------------------------------------
```

```python
Self-Reference > Suite 1 > Case 1

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def crust():
...   print("70km")
...   def mantle():
...       print("2900km")
...       def core():
...           print("5300km")
...           return mantle()
...       return core
...   return mantle
>>> drill = crust
>>> drill = drill()
? 70km

>>> drill = drill()
? 2900km

>>> drill = drill()
(line 1)? 5300km
(line 2)? 2900km

>>> drill()
(line 1)? 5300km
(line 2)? 2900km
(line 3)? Function

---------------------------------------------------------------------
```