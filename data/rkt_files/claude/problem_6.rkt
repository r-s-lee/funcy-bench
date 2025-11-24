#lang racket

    ; Problem: Climbing Stairs
    ; Count distinct ways to climb n stairs with 1 or 2 steps

    (define (solve n)
    ; Base cases for 0 and 1 steps
    (cond 
        [(<= n 0) 0]
        [(= n 1) 1]
        [(= n 2) 2]
        
        ; Dynamic programming approach
        [else
        (let* ([dp (make-vector (+ n 1) 0)])
        ; Initialize first two steps
        (vector-set! dp 1 1)
        (vector-set! dp 2 2)
        
        ; Compute ways for remaining steps
        (for ([i (in-range 3 (add1 n))])
            (vector-set! dp i 
                        (+ (vector-ref dp (- i 1))
                            (vector-ref dp (- i 2)))))
        
        ; Return total ways
        (vector-ref dp n))]))
        
(print (equal? (solve 2) 2))
(print (equal? (solve 3) 3))
(print (equal? (solve 5) 8))
(print (equal? (solve 10) 89))
(print (equal? (solve 20) 10946))
