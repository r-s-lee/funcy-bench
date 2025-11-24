
#lang racket

(define (solve nums)
  (let loop ([nums nums] [max-so-far (car nums)])
    (cond
      [(null? nums) max-so-far]
      [(let ([curr (max (car nums) (+ max-so-far (car nums)))])
           (loop (cdr nums) (max max-so-far curr))))])))

(print (equal? (solve `(-2 1 -3 4 -1 2 1 -5 4)) 6))
(print (equal? (solve `(1)) 1))
(print (equal? (solve `(5 4 -1 7 8)) 23))
(print (equal? (solve `(-1 -2 -3)) -1))
(print (equal? (solve `(10 -1 -1 10)) 18))
