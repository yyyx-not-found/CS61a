# Q1
```scheme
---------------------------------------------------------------------
wwsd-macros > Suite 1 > Case 1

scm> +
? #[+]

scm> list
? #[list]

scm> (define-macro (f x) (car x))
? f

scm> (f (2 3 4)) ; type SchemeError for error, or Nothing for nothing
? 2

scm> (f (+ 2 3))
? #[+]

scm> (define x 2000)
? x

scm> (f (x y z))
? 2000

scm> (f (list 2 3 4))
? #[list]

scm> (f (quote (2 3 4)))
? SchemeError

scm> (define quote 7000)
? quote

scm> (f (quote (2 3 4)))
? 7000

---------------------------------------------------------------------
wwsd-macros > Suite 1 > Case 2

scm> (define-macro (g x) (+ x 2))
? g

scm> (g 2)
? 4

scm> (g (+ 2 3))
? SchemeError

scm> (define-macro (h x) (list '+ x 2))
? h

scm> (h (+ 2 3))
? 7

---------------------------------------------------------------------
wwsd-macros > Suite 1 > Case 3

scm> (define-macro (if-else-5 condition consequent) `(if ,condition ,consequent 5))
? if-else-5

scm> (if-else-5 #t 2)
? 2

scm> (if-else-5 #f 3)
? 5

scm> (if-else-5 #t (/ 1 0))
? SchemeError

scm> (if-else-5 #f (/ 1 0))
? 5

scm> (if-else-5 (= 1 0) 2)
? 5

---------------------------------------------------------------------
```

# Q2
```scheme
---------------------------------------------------------------------
quasiquote > Suite 1 > Case 1

scm> '(1 x 3)
? (1 x 3)

scm> (define x 2)
? x

scm> `(1 x 3)
? (1 x 3)

scm> `(1 ,x 3)
? (1 2 3)

scm> '(1 ,x 3)
? (1 (unquote x) 3)

scm> `(,1 x 3)
? (1 x 3)

scm> `,(+ 1 x 3)
? 6

scm> `(1 (,x) 3)
? (1 (2) 3)

scm> `(1 ,(+ x 2) 3)
? (1 4 3)

scm> (define y 3)
? y

scm> `(x ,(* y x) y)
? (x 6 y)

scm> `(1 ,(cons x (list y 4)) 5)
? (1 (2 3 4) 5)

---------------------------------------------------------------------
```