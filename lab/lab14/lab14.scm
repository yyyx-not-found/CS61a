(define (split-at lst n)
	(define (helper lst res n)
		(if (null? lst)
			(cons res nil)
			(if (> n 0)
				(helper (cdr lst) (append res (list (car lst))) (- n 1))
				(cons res lst)
			)
		)
	)
	(helper lst nil n)
)


; This is not the correct answer
(define-macro (switch expr cases)
	(cons 'cond
		(map (lambda (case) (cons `(equal? ,expr ,(car case)) (cdr case)))
    			cases))
)