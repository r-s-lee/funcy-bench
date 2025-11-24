#lang racket

(define (solve nums target)
  (let loop ([nums nums] [seen (make-hash)])
    (cond
      [(null? nums) #f]
      [(hash-has-key? seen (- target (car nums)))
       (let ([complement (- target (car nums))])
         (list (hash-ref seen complement) 0))]
       )
      [else (hash-set! seen (car nums) (length nums) - 1)
            (loop (cdr nums) seen)])))
(print (equal? (solve `(2 7 11 15) 9) `(0 1)))
(print (equal? (solve `(3 2 4) 6) `(1 2)))
(print (equal? (solve `(3 3) 6) `(0 1)))
(print (equal? (solve `(1 5 5 3) 10) `(1 2)))
(print (equal? (solve `(0 0 4 -2 2) 2) `(2 3)))
