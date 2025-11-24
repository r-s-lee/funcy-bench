#lang racket

    ; Problem: Count distinct ways to climb a staircase of n steps.

    (define (solve n)
    (define dp (make-vector (+ n 1) 0))
    (vector-set! dp 1 1)
    (if (>= n 2) (vector-set! dp 2 2))
    (for ([i (in-range 3 (+ n 1))])
        (vector-set! dp i (+ (vector-ref dp (- i 1)) (vector-ref dp (- i 2)))))
    (vector-ref dp n))

    
(print (equal? (solve `(-2 1 -3 4 -1 2 1 -5 4)) 6))
(print (equal? (solve `(1)) 1))
(print (equal? (solve `(5 4 -1 7 8)) 23))
(print (equal? (solve `(-1 -2 -3)) -1))
(print (equal? (solve `(10 -1 -1 10)) 18))
