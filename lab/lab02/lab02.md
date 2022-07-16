# Q1
```python
---------------------------------------------------------------------
Lambda the Free > Suite 1 > Case 1

Q: Which of the following statements describes a difference between a def statement
and a lambda expression?
Choose the number of the correct choice:
0) A def statement can only have one line in its body.
1) A lambda expression cannot have more than two parameters.
2) A lambda expression does not automatically bind the function object that it returns to any name.
3) A lambda expression cannot return another function.
? 2

---------------------------------------------------------------------
Lambda the Free > Suite 1 > Case 2

Q: How many parameters does the following lambda expression have?
lambda a, b: c + d
Choose the number of the correct choice:
0) Not enough information
1) two
2) three
3) one
? 1

---------------------------------------------------------------------
Lambda the Free > Suite 1 > Case 3

Choose the number of the correct choice:
0) When the lambda expression is evaluated.
1) When you pass the lambda expression into another function.
2) When the function returned by the lambda expression is called.
3) When you assign the lambda expression to a name.
? 2

---------------------------------------------------------------------
Lambda the Free > Suite 2 > Case 1

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> lambda x: x  # A lambda expression with one parameter x
? Function

>>> a = lambda x: x  # Assigning a lambda function to the name a
>>> a(5)
? 5

>>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
? 3

>>> b = lambda x: lambda: x  # Lambdas can return other lambdas!
>>> c = b(88)
>>> c
? Function

>>> c()
? 88

>>> d = lambda f: f(4)  # They can have functions as arguments as well
>>> def square(x):
...     return x * x
>>> d(square)
? 16

---------------------------------------------------------------------
Lambda the Free > Suite 2 > Case 2

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> x = None # remember to review the rules of WWPD given above!
>>> x
>>> lambda x: x
? Function

---------------------------------------------------------------------
Lambda the Free > Suite 2 > Case 3

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> #
>>> # Pay attention to the scope of variables
>>> z = 3
>>> e = lambda x: lambda y: lambda: x + y + z
>>> e(0)(1)()
? 4

>>> f = lambda z: x + z
>>> f(3)
? Error

---------------------------------------------------------------------
Lambda the Free > Suite 2 > Case 4

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> # Try drawing an environment diagram if you get stuck!
>>> higher_order_lambda = lambda f: lambda x: f(x)
>>> g = lambda x: x * x
>>> higher_order_lambda(2)(g) # Which argument belongs to which function call?
? Error

>>> higher_order_lambda(g)(2)
? 4

>>> call_thrice = lambda f: lambda x: f(f(f(x)))
>>> call_thrice(lambda y: y + 1)(0)
? 3

>>> print_lambda = lambda z: print(z)
>>> print_lambda
? Function

>>> one_thousand = print_lambda(1000)
? 1000

>>> one_thousand
? Nothing

---------------------------------------------------------------------
```

# Q2
```python
---------------------------------------------------------------------
Higher Order Functions > Suite 1 > Case 1

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def even(f):
...     def odd(x):
...         if x < 0:
...             return f(-x)
...         return f(x)
...     return odd
>>> steven = lambda x: x
>>> stewart = even(steven)
>>> stewart
? Function

>>> stewart(61)
? 61

>>> stewart(-4)
? 4

---------------------------------------------------------------------
Higher Order Functions > Suite 1 > Case 2

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def cake():
...    print('beets')
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
>>> chocolate = cake()
? beets

>>> chocolate
? Function

>>> chocolate()
(line 1)? sweets
(line 2)? 'cake'

>>> more_chocolate, more_cake = chocolate(), cake
? sweets

>>> more_chocolate
? 'cake'

>>> def snake(x, y):
...    if cake == more_cake:
...        return chocolate
...    else:
...        return x + y
>>> snake(10, 20)
? Function

>>> snake(10, 20)()
(line 1)? sweets
(line 2)? 'cake'

>>> cake = 'cake'
>>> snake(10, 20)
? 30

---------------------------------------------------------------------
```

# Q6-Q7
Please copy you code into [PythonTutor](https://pythontutor.com/composingprograms.html#mode=edit)!