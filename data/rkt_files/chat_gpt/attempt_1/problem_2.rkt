#lang racket

; Problem: Given an integer x, return true if x is a palindrome.

; Solution:
; Compare the number with its reverse without converting to a string.

(define (solve x)
  (if (< x 0)
      #f
      (let loop ([original x] [reversed 0])
        (if (= original 0)
            (= x reversed)
            (loop (quotient original 10)
                  (+ (* reversed 10) (remainder original 10)))))))

(print (equal? (solve 121) #t))
(print (equal? (solve -121) #f))
(print (equal? (solve 10) #f))
(print (equal? (solve 0) #t))
(print (equal? (solve 1234321) #t))
