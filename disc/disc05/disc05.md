# 1.4
```
• What does the expression evaluate to?
• Does the expression violate any abstraction barriers? If so, write an equivalent
expression that does not violate abstraction barriers.

1. label(t)
• the value of tree node
• no
2. t[0]
• the value of tree node
• yes; label(t)
3. label(branches(t)[0])
• value of first branch
• no
4. label(branches(t))
• first branch
• yes; branches(t)[0]
5. is_leaf(t[1:][1])
• whether the second branch is leaf
• yes; is_leaf(branches(t)[1])
6. [label(b) for b in branches(t)]
• list of the values of branches
• no
7. Challenge: branches(tree(2, tree(t, [])))[0]
• t
• no
```

# 2.1
```python
>>> lst1 = [1, 2, 3]
>>> lst2 = lst1
>>> lst1 is lst2
True
>>> lst2.extend([5, 6])
>>> lst1[4]
6
>>> lst1.append([-1, 0, 1])
>>> -1 in lst1
False
>>> lst2[5]
[-1, 0, 1]
>>> lst3 = lst2[:]
>>> lst3.insert(3, lst2.pop(3))
>>> len(lst1)
5
>>> lst1[4] is lst3[6]
True
>>> lst3[lst2[4][1]]
1
>>> lst1[:3] is lst2[:3]
False
>>> lst1[:3] == lst2[:3]
True
>>> x = (1, 2, [4, 5, 6])
>>> x[2] = [3, 5, 6]
Error
>>> x
(1, 2, [4, 5, 6])
>>> x[2][0] = 3
>>> x
(1, 2, [3, 5, 6])
```