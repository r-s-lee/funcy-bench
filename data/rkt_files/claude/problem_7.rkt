#lang racket

    ; Problem: Maximum Subarray
    ; Find contiguous subarray with largest sum using Kadane's algorithm

    (define (solve nums)
    ; Kadane's algorithm for maximum subarray sum
    (let loop ([max-sum (car nums)]
                [current-sum (car nums)]
                [rest (cdr nums)])
        (if (null? rest)
            max-sum
            (let* ([next-num (car rest)]
                [new-current (max next-num (+ current-sum next-num))]
                [new-max (max max-sum new-current)])
            (loop new-max new-current (cdr rest))))))
(print (equal? (solve `(-2 1 -3 4 -1 2 1 -5 4)) 6))
(print (equal? (solve `(1)) 1))
(print (equal? (solve `(5 4 -1 7 8)) 23))
(print (equal? (solve `(-1 -2 -3)) -1))
(print (equal? (solve `(10 -1 -1 10)) 18))
