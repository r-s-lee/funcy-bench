#lang racket
(define (solve nums)
  (let loop ([nums nums] [max-so-far 0] [max-ending-here 0])
    (cond
      [(null? nums) max-so-far]
      [else (set! max-ending-here (max 0 (+ max-ending-here (car nums))))
            (set! max-so-far (max max-so-far max-ending-here))
            (loop (cdr nums) max-so-far max-ending-here)])))
(print (equal? (solve `(-2 1 -3 4 -1 2 1 -5 4)) 6))
(print (equal? (solve `(1)) 1))
(print (equal? (solve `(5 4 -1 7 8)) 23))
(print (equal? (solve `(-1 -2 -3)) -1))
(print (equal? (solve `(10 -1 -1 10)) 18))
