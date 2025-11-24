#lang racket

; Problem: Given an integer x, return true if x is a palindrome.

; Solution:
; Use two pointers to compare digits from the front and back.

(define (solve x)
  (define digits (number->string x))
  (let loop ([start 0] [end (- (string-length digits) 1)])
    (cond
      [(>= start end) #t]
      [(not (char=? (string-ref digits start) (string-ref digits end))) #f]
      [else (loop (add1 start) (sub1 end))])))

(print (equal? (solve 121) #t))
(print (equal? (solve -121) #f))
(print (equal? (solve 10) #f))
(print (equal? (solve 0) #t))
(print (equal? (solve 1234321) #t))
