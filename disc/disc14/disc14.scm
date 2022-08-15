(define (append-stream s1 s2)
    (cond 
        ((and (null? s1) (null? s2)) nil)
        ((null? s1) (append-stream s2 nil))
        (else (cons-stream (car s1) (append-stream (cdr-stream s1) s2)))
    )
)


(define (deep-map fn lst)
    (cond
        ((null? lst) nil)
        ((list? (car lst)) (cons (deep-map fn (car lst)) (deep-map fn (cdr lst))))
        (else (cons (fn (car lst)) (deep-map fn (cdr lst))))
    )
)


(define (sum lst)
    (define (helper lst res)
        (if (null? lst)
            res
            (helper (cdr lst) (+ (car lst) res))
        )
    )
    (helper lst 0)
)