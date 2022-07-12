;;;3

;;3.1.1
(define a (+ 1 2)) ;a
a ;3
(define b (+ (* 3 3) (* 4 4))) ;b
(+ a b) ;28
(= (modulo 10 3) (quotient 5 3)) ;#t quotient is different from '/' operator
(even? (+ (- (* 5 4) 3) 2)) ;#f


;;;4

;;4.1.1
(if (or #t (/ 1 0)) 1 (/ 1 0)) ;1
(if (> 4 3) (+ 1 2 3 4) (+ 3 4 (* 3 2))) ;10
((if (< 4 3) + -) 4 100) ;-96
(if 0 1 2) ;1
;;4.2.1
(define (factorial x)
    (if (= x 0) 
        1
        (* x (factorial (- x 1)))
    )
)
;;4.2.2
(define (fib x)
    (if (< x 2) 
        x
        (+ (fib (- x 1)) (fib (- x 2)))
    )
)

;;;5
;;5.1.1
(define (my-append a b)
    (if (null? (cdr a)) 
        (cons (car a) b)
        (cons (car a) (my-append (cdr a) b))
    )
)
;;5.1.2
;begin with 0
(define (insert element lst index)
    (if (= 0 index)
        (cons element lst)
        (cons (car lst) (insert element (cdr lst) (- index 1)))
    )
)
;;5.1.3
(define (duplicate lst)
    (if (null? (cdr lst))
        (cons (car lst) (list (car lst)))
        (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
    )
)