#lang racket

; Problem: Remove Duplicates from Sorted Array
; Alternative solution using set operations and functional approach

(define (solve nums)
  ; Use set to track unique elements efficiently
  (define unique-set (apply set nums))
  
  ; Convert set back to sorted list and count
  (set-count unique-set))
(print (equal? (solve `(1 1 2)) 2))
(print (equal? (solve `(0 0 1 1 1 2 2 3 3 4)) 5))
(print (equal? (solve `(1 1 1 1)) 1))
(print (equal? (solve `(1 2 3)) 3))
(print (equal? (solve `(1)) 1))
