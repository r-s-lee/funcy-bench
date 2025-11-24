#lang racket
(define (solve x)
  (let loop ([x x] [rev 0])
    (cond
      [(zero? x) (= x rev)]
      [(< (abs rev) (expt 2 31))
       (loop (quotient x 10) (+ (* rev 10) (modulo x 10)))]
      [else #f])))
(print (equal? (solve 121) #t))
(print (equal? (solve -121) #f))
(print (equal? (solve 10) #f))
(print (equal? (solve 0) #t))
(print (equal? (solve 1234321) #t))
