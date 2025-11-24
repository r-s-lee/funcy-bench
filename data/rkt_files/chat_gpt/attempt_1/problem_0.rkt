#lang racket

; Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

; Solution:
; Iterate through the list with nested loops to check every pair of indices.

(define (solve nums target)
  (for*/first ([i (in-range (length nums))]
               [j (in-range (add1 i) (length nums))]
               #:when (= (+ (list-ref nums i) (list-ref nums j)) target))
    (list i j)))

(print (equal? (solve `(2 7 11 15) 9) `(0 1)))
(print (equal? (solve `(3 2 4) 6) `(1 2)))
(print (equal? (solve `(3 3) 6) `(0 1)))
(print (equal? (solve `(1 5 5 3) 10) `(1 2)))
(print (equal? (solve `(0 0 4 -2 2) 2) `(2 3)))
