#lang racket

; Problem: Given an integer array nums, find the contiguous subarray with the largest sum and return its sum.

; Solution:
; Use Kadane's algorithm for O(n) time complexity.

(define (solve nums)
  (let loop ([current-max (list-ref nums 0)]
             [global-max (list-ref nums 0)]
             [i 1])
    (if (>= i (length nums))
        global-max
        (let ([new-current-max (max (list-ref nums i) (+ current-max (list-ref nums i)))])
          (loop new-current-max (max global-max new-current-max) (add1 i))))))

(print (equal? (solve `(-2 1 -3 4 -1 2 1 -5 4)) 6))
(print (equal? (solve `(1)) 1))
(print (equal? (solve `(5 4 -1 7 8)) 23))
(print (equal? (solve `(-1 -2 -3)) -1))
(print (equal? (solve `(10 -1 -1 10)) 18))
