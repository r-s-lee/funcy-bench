#lang racket

; Problem: Two Sum
; Third solution using higher-order functions and generator-like approach

(define (solve nums target)
  ; Generate all possible index pairs
  (define (generate-index-pairs nums)
    (for*/first ([i (in-range (length nums))]
                 [j (in-range (add1 i) (length nums))]
                 #:when (= (+ (list-ref nums i) 
                              (list-ref nums j)) 
                           target))
      (list i j)))
  
  (generate-index-pairs nums))
(print (equal? (solve `(2 7 11 15) 9) `(0 1)))
(print (equal? (solve `(3 2 4) 6) `(1 2)))
(print (equal? (solve `(3 3) 6) `(0 1)))
(print (equal? (solve `(1 5 5 3) 10) `(1 2)))
(print (equal? (solve `(0 0 4 -2 2) 2) `(2 3)))
