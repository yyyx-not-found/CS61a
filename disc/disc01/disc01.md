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

# 2.1
![avatar](./pictures/2.1-step01.png)
![avatar](./pictures/2.1-step02.png) 
![avatar](./pictures/2.1-step03.png)

# 2.2
![avatar](./pictures/2.2-step01.png)
![avatar](./pictures/2.2-step02.png)
![avatar](./pictures/2.2-step03.png)
![avatar](./pictures/2.2-step04.png)

# 2.3
![avatar](./pictures/2.3-step01.png)
![avatar](./pictures/2.3-step02.png)
![avatar](./pictures/2.3-step03.png)
![avatar](./pictures/2.3-step04.png)
![avatar](./pictures/2.3-step05.png)
![avatar](./pictures/2.3-step06.png)
![avatar](./pictures/2.3-step07.png)
![avatar](./pictures/2.3-step08.png)
![avatar](./pictures/2.3-step09.png)
![avatar](./pictures/2.3-step10.png)

# 2.4
![avatar](./pictures/2.4-step01.png)
![avatar](./pictures/2.4-step02.png)
![avatar](./pictures/2.4-step03.png)
![avatar](./pictures/2.4-step04.png)
![avatar](./pictures/2.4-step05.png)
![avatar](./pictures/2.4-step06.png)
![avatar](./pictures/2.4-step07.png)
![avatar](./pictures/2.4-step08.png)
![avatar](./pictures/2.4-step09.png)
![avatar](./pictures/2.4-step10.png)
![avatar](./pictures/2.4-step11.png)
![avatar](./pictures/2.4-step12.png)
![avatar](./pictures/2.4-step13.png)
![avatar](./pictures/2.4-step14.png)
![avatar](./pictures/2.4-step15.png)
![avatar](./pictures/2.4-step16.png)
![avatar](./pictures/2.4-step17.png)
![avatar](./pictures/2.4-step18.png)
![avatar](./pictures/2.4-step19.png)

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