(define (cddr s)
    (cdr (cdr s))
)

(define (cadr s)
    (car (cdr s))
)

(define (caddr s)
    (car (cdr (cdr s)))
)

(define (sign num)
    (cond
        ((> num 0) 1)
        ((< num 0) -1)
        (else 0)
    )
)


(define (square x) 
    (* x x)
)

(define (pow x y)
    (cond 
        ((= 0 y) 1)
        ((odd? y) (* x (square (pow x (/ (- y 1) 2)))))
        ((even? y) (square (pow x (/ y 2))))
    )
)


(define (unique s)
    (define (lst-filter lst res)
        (if (null? lst)
            res
            (if (repeat res (car lst))
                (lst-filter (cdr lst) res)
                (lst-filter (cdr lst) (append res (list (car lst))))
            )
        )    
    )

    (define (repeat lst item) 
        (if (null? lst)
            #f
            (if (equal? (car lst) item)
                #t
                (repeat (cdr lst) item)
            )    
        )
    )

    (lst-filter s nil)
)


(define (replicate x n)
    (define (iter cur res)
        (if (= cur n)
            res
            (iter (+ cur 1) (cons x res))
        )
    )

    (iter 0 nil)
)


(define (accumulate combiner start n term)
    (if (= 0 n)
        start
        (combiner (term n) (accumulate combiner start (- n 1) term))    
    )
)

(define (accumulate-tail combiner start n term)
    (define (iter cur res)
        (if (> cur n)
            res
            (iter (+ cur 1) (combiner res (term cur)))
        )    
    )

    (iter 1 start)
)


(define-macro (list-of map-expr for var in lst if filter-expr)
    ;(map (lambda (x) (if filter-expr map-expr nil)) lst)
    `(lst-filter (map (lambda (,var) (if ,filter-expr ,map-expr nil)) ,lst))
)

(define (lst-filter lst)
        (if (null? lst)
            nil
            (if (null? (car lst))
                (lst-filter (cdr lst))
                (cons (car lst) (lst-filter (cdr lst)))
            )
        )    
    )


