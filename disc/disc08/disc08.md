# 1.1
```python
What would Python display? If a StopIteration Exception occurs, write StopIteration,
and if another error occurs, write Error.

>>> lst = [6, 1, "a"]
>>> next(lst)
Error

>>> lst_iter = iter(lst)
>>> next(lst_iter)
6

>>> next(lst_iter)
1

>>> next(iter(lst))
6

>>> [x for x in lst_iter]
['a']

```

# 3.1
```python
class Student:
    students = 0 # this is a class attribute
    def __init__(self, name, ta):
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        ta.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1


What will the following lines output?

>>> callahan = Professor("Callahan")
>>> elle = Student("Elle", callahan)
There are now 1 students

>>> elle.visit_office_hours(callahan)
Thanks, Callahan

>>> elle.visit_office_hours(Professor("Paulette"))
Thanks, Paulette

>>> elle.understanding
2

>>> [name for name in callahan.students]
['Elle']

>>> x = Student("Vivian", Professor("Stromwell")).name
There are now 2 students

>>> x
'Vivian'

>>> [name for name in callahan.students]
['Elle']

```

# 4.3
```python
class A:
    def f(self):
        return 2

    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)

class B(A):
    def f(self):
        return 4


What would Python display?

>>> x, y = A(), B()
>>> x.f()
2

>>> B.f()
Error

>>> x.g(x, 1)
4

>>> y.g(x, 2)
8

```