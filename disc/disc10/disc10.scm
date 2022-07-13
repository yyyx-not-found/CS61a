(define (factorial x)
    (if (= x 0) 
        1
        (* x (factorial (- x 1)))
    )
)


(define (fib x)
    (if (< x 2) 
        x
        (+ (fib (- x 1)) (fib (- x 2)))
    )
)


(define (my-append a b)
    (if (null? (cdr a)) 
        (cons (car a) b)
        (cons (car a) (my-append (cdr a) b))
    )
)


;begin with 0
(define (insert element lst index)
    (if (= 0 index)
        (cons element lst)
        (cons (car lst) (insert element (cdr lst) (- index 1)))
    )
)


(define (duplicate lst)
    (if (null? (cdr lst))
        (cons (car lst) (list (car lst)))
        (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
    )
)