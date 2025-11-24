#lang racket

    ; Problem: Remove duplicates from a sorted array in-place and return the new length.

    (define (solve nums)
    (define n (length nums))
    (if (= n 0)
        0
        (let loop ([i 1] [last 0])
            (if (< i n)
                (if (= (list-ref nums last) (list-ref nums i))
                    (loop (+ i 1) last)
                    (begin
                    (set! nums (+ last 1) (list-ref nums i))
                    (loop (+ i 1) (+ last 1))))
                (+ last 1)))))

    
(print (equal? (solve 2) 2))
(print (equal? (solve 3) 3))
(print (equal? (solve 5) 8))
(print (equal? (solve 10) 89))
(print (equal? (solve 20) 10946))
