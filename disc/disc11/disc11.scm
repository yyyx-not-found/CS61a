;;;1

;;1.1
;yes yes
(define (question-b x y)
    (if (= x 0) y
    (question-b (- x 1) (+ y x))))
;yes yes
(define (question-c x y)
    (if (> x y)
        (question-c (- y 1) x)
        (question-c (+ x 10) y)))
;yes yes
(define (question-d n)
    (if (question-d n)
        (question-d (- n 1))
        (question-d (+ n 10))))
;yes no
(define (question-e n)
    (cond 
        ((= n 0) 1)
        ((question-e (- n 1)) (question-e (- n 2)))
        (else (begin (print 2) (question-e (- n 3))))
    )
)
;;1.2
(define (reverse lst)
    (define (iter lst res) 
        (if (null? lst)
            res
            (iter (cdr lst) (cons (car lst) res))
        )
    )

    (iter lst nil)
)
;;1.3
(define (insert n lst)
    (define (iter lst item res)
        (if (null? lst)
            (append res (list item))
            (if (< (car lst) item)
                (iter (cdr lst) item (append res (list (car lst))))
                (append res (cons item lst))
            )
        )
    )

    (iter lst n nil)
)


;;;3

;;3.1
(define-macro (or-macro expr1 expr2)
    `(let ((v1 ,expr1))
        (if v1
            v1
            ,expr2
        )
    )
)
;;3.2
(define-macro (prune-expr expr)
    `(print
        ,(cons
            (car expr) 
            (cons 
                (car (cdr expr)) 
                (cdr (cdr (cdr expr)))
            )
        )
    )
)
;;3.3
(define-macro (when condition exprs)
    (list 'if condition 
        (cons 'begin exprs)
        ''okey
    )
)

(define-macro (when condition exprs)
    `(if ,condition ,(cons 'begin exprs) 'okey)
)
