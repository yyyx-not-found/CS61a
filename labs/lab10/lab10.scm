(define (over-or-under num1 num2)
    (if (< num1 num2) -1 
        (if (> num1 num2) 1 0))
)


(define (filter-lst fn lst)
    (if (null? lst) 
            lst
            (if (fn (car lst)) 
                (cons (car lst) (filter-lst fn (cdr lst)))
                (filter-lst fn (cdr lst)))
    )
)


(define (make-adder num)
    (lambda (x) (+ num x))
)


(define lst
    (cons '(1) (cons 2 (cons '(3 4) '(5))))
)


(define (composed f g)
    (lambda (x) (f (g x)))
)


(define (remove item lst)
    (define fn (lambda (x) (not (= x item))))
    (filter-lst fn lst)
)


(define (no-repeats s)
    (if (or (null? s) (null? (remove (car s) s)))
        (if (null? s) nil (list (car s)))
        (cons (car s) (no-repeats (remove (car s) s)))
    )
)


(define (substitute s old new)
    (define fn (lambda (x) (equal? x old)))
    (if (null? s) 
            s
            (if (fn (car s)) 
                (cons new (substitute (cdr s) old new))
                (if (list? (car s))
                    (cons (substitute (car s) old new) (substitute (cdr s) old new))
                    (cons (car s) (substitute (cdr s) old new))
                )
            )
    )
)


(define (sub-all s olds news)
    (if (null? olds) 
        s
        (substitute (sub-all s (cdr olds) (cdr news)) (car olds) (car news))
    )
)

