#lang racket

    ; Problem: Return indices of two numbers in an array such that they add up to a given target.

    (define (solve nums target)
    (define ht (make-hash))
    (for ([i (in-range (length nums))])
        (let ([complement (- target (list-ref nums i))])
        (if (hash-has-key? ht complement)
            (list (hash-ref ht complement) i)
            (hash-set! ht (list-ref nums i) i)))))

    
(print (equal? (solve `(2 7 11 15) 9) `(0 1)))
(print (equal? (solve `(3 2 4) 6) `(1 2)))
(print (equal? (solve `(3 3) 6) `(0 1)))
(print (equal? (solve `(1 5 5 3) 10) `(1 2)))
(print (equal? (solve `(0 0 4 -2 2) 2) `(2 3)))
