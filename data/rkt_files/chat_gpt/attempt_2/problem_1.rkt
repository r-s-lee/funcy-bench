#lang racket

; Problem: Given a signed 32-bit integer x, return x with its digits reversed.

; Solution:
; Convert the number to a list of digits, reverse it, and rebuild the number.

(define (solve x)
  (define (number->digits n)
    (if (= n 0)
        '()
        (cons (remainder n 10) (number->digits (quotient n 10)))))
  (define (digits->number digits)
    (foldl (lambda (digit acc) (+ (* acc 10) digit)) 0 digits))
  (let ([reversed (digits->number (reverse (number->digits (abs x))))])
    (if (or (< reversed -2147483648) (> reversed 2147483647))
        0
        (if (< x 0) (- reversed) reversed))))

(print (equal? (solve 123) 321))
(print (equal? (solve -123) -321))
(print (equal? (solve 120) 21))
(print (equal? (solve 1534236469) 0))
(print (equal? (solve -2147483648) 0))
