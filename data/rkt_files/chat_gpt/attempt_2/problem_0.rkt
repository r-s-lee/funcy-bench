#lang racket

; Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

; Solution:
; Use recursion to search for the solution.

(define (solve nums target)
  (define (find-pair i)
    (if (= i (length nums))
        '()
        (let loop ([j (add1 i)])
          (cond
            [(= j (length nums)) (find-pair (add1 i))]
            [(= (+ (list-ref nums i) (list-ref nums j)) target) (list i j)]
            [else (loop (add1 j))]))))
  (find-pair 0))

(print (equal? (solve `(2 7 11 15) 9) `(0 1)))
(print (equal? (solve `(3 2 4) 6) `(1 2)))
(print (equal? (solve `(3 3) 6) `(0 1)))
(print (equal? (solve `(1 5 5 3) 10) `(1 2)))
(print (equal? (solve `(0 0 4 -2 2) 2) `(2 3)))
