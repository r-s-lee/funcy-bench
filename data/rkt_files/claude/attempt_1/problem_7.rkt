#lang racket

; Problem: Maximum Subarray
; Alternative solution using functional folding approach

(define (solve nums)
  ; Functional fold to compute maximum subarray sum
  (first 
   (foldl 
    (lambda (current-num acc)
      (define current-sum (first acc))
      (define max-sum (second acc))
      (define new-sum (max current-num (+ current-sum current-num)))
      (define new-max (max max-sum new-sum))
      (list new-sum new-max))
    (list (car nums) (car nums))
    (cdr nums))))
(print (equal? (solve `(-2 1 -3 4 -1 2 1 -5 4)) 6))
(print (equal? (solve `(1)) 1))
(print (equal? (solve `(5 4 -1 7 8)) 23))
(print (equal? (solve `(-1 -2 -3)) -1))
(print (equal? (solve `(10 -1 -1 10)) 18))
