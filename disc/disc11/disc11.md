# 1.1
```scheme
;1
(define (question-b x y)
    (if (= x 0) 
        y
        (question-b (- x 1) (+ y x))
    )
)


;2
(define (question-c x y)
    (if (> x y)
        (question-c (- y 1) x)
        (question-c (+ x 10) y)
    )
)


3;
(define (question-d n)
    (if (question-d n)
        (question-d (- n 1))
        (question-d (+ n 10))
    )
)


;4
(define (question-e n)
    (cond ((= n 0) 1)
        ((question-e (- n 1)) (question-e (- n 2)))
        (else (begin (print 2) (question-e (- n 3))))
    )
)
```
| No. | recursive call | constant frame |
|--|--|--|
| 1 | True | True |
| 2 | True | True |
| 3 | True | True |
| 4 | True | False |