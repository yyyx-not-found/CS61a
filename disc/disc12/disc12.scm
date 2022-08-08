(define (map-stream f s)
    (if (null? s)
        nil
        (cons-stream (f (car s)) (map-stream f (cdr-stream s)))
    )
)


(define (slice s start end)
    (define (find-start s n)
        (if (or (= 0 n) (null? s))
            s
            (find-start (cdr-stream s) (- n 1))
        )
    )
    (define (slicing s n)
        (if (or (= 0 n) (null? s))
            nil
            (cons (car s) (slicing (cdr-stream s) (- n 1)))
        )
    )

    (slicing (find-start s start) (- end start))
)


(define (combine-with f xs ys)
    (if (or (null? xs) (null? ys))
        nil
        (cons-stream
            (f (car xs) (car ys))
            (combine-with f (cdr-stream xs) (cdr-stream ys))
        )
    )
)


(define (naturals start) 
    (cons-stream start (naturals (+ start 1)))
)

(define nat (naturals 0))