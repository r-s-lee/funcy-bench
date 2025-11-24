#lang racket

; Problem: Given a signed 32-bit integer x, return x with its digits reversed.

; Solution:
; Convert the number to a string, reverse the digits, and check bounds.

(define (solve x)
  (define reversed (string->number (string-reverse (number->string (abs x)))))
  (if (< x 0)
      (set! reversed (- reversed)))
  (if (<= -2147483648 reversed 2147483647)
      reversed
      0))

(print (equal? (solve 123) 321))
(print (equal? (solve -123) -321))
(print (equal? (solve 120) 21))
(print (equal? (solve 1534236469) 0))
(print (equal? (solve -2147483648) 0))
