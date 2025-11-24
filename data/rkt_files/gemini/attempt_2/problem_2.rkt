
#lang racket

(define (solve x)
  (string=? (string x) (string-reverse (string x))))

(print (equal? (solve 121) #t))
(print (equal? (solve -121) #f))
(print (equal? (solve 10) #f))
(print (equal? (solve 0) #t))
(print (equal? (solve 1234321) #t))
