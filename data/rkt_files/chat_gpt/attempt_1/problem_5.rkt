#lang racket

; Problem: Given an array of integers nums, remove duplicates in-place such that each element appears only once and return the new length.

; Solution:
; Traverse the array, maintaining a pointer for the unique elements.

(define (solve nums)
  (define unique-count 0)
  (for ([i (in-range (length nums))])
    (when (or (= i 0) (not (= (list-ref nums i) (list-ref nums (- i 1)))))
      (set! nums (vector-set! nums unique-count (list-ref nums i)))
      (set! unique-count (add1 unique-count))))
  unique-count)

(print (equal? (solve `(1 1 2)) 2))
(print (equal? (solve `(0 0 1 1 1 2 2 3 3 4)) 5))
(print (equal? (solve `(1 1 1 1)) 1))
(print (equal? (solve `(1 2 3)) 3))
(print (equal? (solve `(1)) 1))
