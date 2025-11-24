
#lang racket

(define (solve n)
  (let loop ([n n] [prev 1] [curr 1])
    (cond
      [(zero? n) prev]
      [else (loop (- n 1) curr (+ prev curr))])))

(print (equal? (solve 2) 2))
(print (equal? (solve 3) 3))
(print (equal? (solve 5) 8))
(print (equal? (solve 10) 89))
(print (equal? (solve 20) 10946))
