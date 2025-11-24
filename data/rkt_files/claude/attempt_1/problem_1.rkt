#lang racket

; Problem: Reverse Integer
; Alternative solution using explicit digit manipulation

(define (solve x)
  ; Handle sign separately
  (define sign (if (negative? x) -1 1))
  (define abs-x (abs x))
  
  ; Recursive digit reversal
  (define (reverse-digits n)
    (let reverse-loop ([current n]
                       [reversed 0])
      (if (zero? current)
          reversed
          (let* ([digit (remainder current 10)]
                 [new-reversed (+ (* reversed 10) digit)])
            (reverse-loop (quotient current 10) new-reversed)))))
  
  ; Compute reversed number and apply sign
  (define result (* sign (reverse-digits abs-x)))
  
  ; Check 32-bit integer constraints
  (if (or (< result (- (expt 2 31))) 
          (>= result (expt 2 31)))
      0
      result))
(print (equal? (solve 123) 321))
(print (equal? (solve -123) -321))
(print (equal? (solve 120) 21))
(print (equal? (solve 1534236469) 0))
(print (equal? (solve -2147483648) 0))
