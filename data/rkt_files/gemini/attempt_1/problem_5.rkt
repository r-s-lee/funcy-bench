
#lang racket

(define (solve nums)
  (let ([n (length nums)])
    (let loop ([i 0] [j 1])
      (cond
        [(>= j n) i]
        [(= (vector-ref nums i) (vector-ref nums j))
         (loop i (add1 j))]
        [else (vector-set! nums (add1 i) (vector-ref nums j))
               (loop (add1 i) (add1 j))])))
    n))

(print (equal? (solve `(1 1 2)) 2))
(print (equal? (solve `(0 0 1 1 1 2 2 3 3 4)) 5))
(print (equal? (solve `(1 1 1 1)) 1))
(print (equal? (solve `(1 2 3)) 3))
(print (equal? (solve `(1)) 1))
