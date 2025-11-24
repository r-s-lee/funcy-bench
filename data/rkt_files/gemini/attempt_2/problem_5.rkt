
#lang racket

(define (solve nums)
  (let loop ([nums nums] [i 0])
    (cond
      [(null? nums) i]
      [(= (car nums) (cadr nums))
       (loop (cdr nums) i)]
      [else (loop (cdr nums) (add1 i))])))

(print (equal? (solve `(1 1 2)) 2))
(print (equal? (solve `(0 0 1 1 1 2 2 3 3 4)) 5))
(print (equal? (solve `(1 1 1 1)) 1))
(print (equal? (solve `(1 2 3)) 3))
(print (equal? (solve `(1)) 1))
