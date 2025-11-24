#lang racket
(define (solve n)
  (let loop ([n n] [a 1] [b 1])
    (cond
      [(zero? n) a]
      [else (loop (- n 1) b (+ a b))])))
(print (equal? (solve 2) 2))
(print (equal? (solve 3) 3))
(print (equal? (solve 5) 8))
(print (equal? (solve 10) 89))
(print (equal? (solve 20) 10946))
