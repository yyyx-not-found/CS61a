# 1.2
```python
>>> def square(x):
...     print("here!")
...     return x * x

>>> def so_slow(num):
...     x = num
...     while x > 0:
...         x = x + 1
...     return x / 0

>>> square(so_slow(5))
Infinite Loop!
```

# 2.1 - 2.4
Copy the code into [PythonTutor](https://pythontutor.com/composingprograms.html#mode=edit) and you will get your answer!

# 3
```python
x = 3
def p(rint):
    print(rint)
def g(x, y):
    if x:
        print("one")
    elif x:
        print(True, x) # Does x being truth-y affect the printed value?
    if y:
        print(True, y) # Does y being truth-y affect the printed value?
    else:
        print(False, y) # Does y being false-y affect the printed value?
    return print(p(y)) + x
```
| Expression | Interactive Output |
|--|--|
| print(4, 5) + 1 | 4 5 <br> Error |
| 2 * 2 * 1 + x * x | 13 |
| print(3 * 3 * 1) | 9 |
| print(x + 1 * x + 1) | 7 |
| print(print(x + 1 * x + 1)) | 7 <br> None |
| print(print(x + 1 * x + 1) + 1) | 7 <br> Error |
| print(p("rint")) | rint <br> None |
| x, y = 2, x <br> g(y, x) | one <br> True 2 <br> 2 <br> None <br> Error|
| g(y, p("rint")) | rint <br> one <br> False None <br> None <br> None <br> Error|