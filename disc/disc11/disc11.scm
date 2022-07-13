(define (reverse lst)
    (define (iter lst res) 
        (if (null? lst)
            res
            (iter (cdr lst) (cons (car lst) res))
        )
    )

    (iter lst nil)
)


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


(define-macro (or-macro expr1 expr2)
    `(let ((v1 ,expr1))
        (if v1
            v1
            ,expr2
        )
    )
)


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


;version one
(define-macro (when condition exprs)
    (list 'if condition 
        (cons 'begin exprs)
        ''okey
    )
)

;version two
(define-macro (when condition exprs)
    `(if ,condition ,(cons 'begin exprs) 'okey)
)
