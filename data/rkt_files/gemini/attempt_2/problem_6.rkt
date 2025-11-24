
#lang racket

(define (solve n)
  (let loop ([n n] [fibs (list 0 1)])
    (cond
      [(zero? n) (car fibs)]
      [else (loop (- n 1) (cdr fibs))]))))

(print (equal? (solve 2) 2))
(print (equal? (solve 3) 3))
(print (equal? (solve 5) 8))
(print (equal? (solve 10) 89))
(print (equal? (solve 20) 10946))
