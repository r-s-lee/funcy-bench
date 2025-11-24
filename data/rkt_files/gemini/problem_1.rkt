#lang racket
(define (solve x)
  (let loop ([x x] [rev 0])
    (cond
      [(zero? x) rev]
      [(< (abs rev) (expt 2 31))
       (loop (quotient x 10) (+ (* rev 10) (modulo x 10)))]
      [else 0])))
(print (equal? (solve 123) 321))
(print (equal? (solve -123) -321))
(print (equal? (solve 120) 21))
(print (equal? (solve 1534236469) 0))
(print (equal? (solve -2147483648) 0))
