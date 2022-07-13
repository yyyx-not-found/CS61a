```
>>>python3 ok -q wwsd_lists -u
```

```scheme
scm> (cons 1 (cons 2 nil))
(1 2)

scm> (car (cons 1 (cons 2 nil)))
1

scm> (cdr (cons 1 (cons 2 nil)))
(2)

scm> (list 1 2 3)
(1 2 3)

scm> '(1 2 3)
(1 2 3)

scm> (cons 1 '(list 2 3))  ; Recall quoting
(1 list 2 3)

scm> (cons 1 `(list 2 3)) ; Quasiquotes also work as quotes!
(1 list 2 3)

scm> '(cons 4 (cons (cons 6 8) ()))
(cons 4 (cons (cons 6 8) ()))

scm> (cons 1 (list (cons 3 nil) 4 5))
(1 (3) 4 5)
```
