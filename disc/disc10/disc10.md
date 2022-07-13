# 3.1
```scheme
scm> (define a (+ 1 2))
a
scm> a
3
scm> (define b (+ (* 3 3) (* 4 4)))
b
scm> (+ a b)
28
scm> (= (modulo 10 3) (quotient 5 3))
#t
scm> (even? (+ (- (* 5 4) 3) 2))
#f
```
# 4.1
```scheme
scm> (if (or #t (/ 1 0)) 1 (/ 1 0))
1
scm> (if (> 4 3) (+ 1 2 3 4) (+ 3 4 (* 3 2)))
10
scm> ((if (< 4 3) + -) 4 100)
-96
scm> (if 0 1 2)
1
```