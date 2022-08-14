(define (rle s)
    (define (helper s prev num)
        (if (null? s)
            (cons-stream (list prev num) nil)
            (if (= (car s) prev)
                (helper (cdr-stream s) prev (+ num 1))
                (cons-stream (list prev num) (helper (cdr-stream s) (car s) 1))
            )
        )
    )
    (if (null? s)
        nil
        (helper (cdr-stream s) (car s) 1)
    )    
)

(define (group-by-nondecreasing s)
    (define (helper s prev sub)
        (if (null? s)
            (cons-stream sub nil)
            (if (< (car s) prev)
                (cons-stream sub (helper (cdr-stream s) (car s) (list (car s))))
                (helper (cdr-stream s) (car s) (append sub (list (car s))))
            )
        )
    )
    (if (null? s)
        nil
        (helper (cdr-stream s) (car s) (list (car s)))
    )
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

