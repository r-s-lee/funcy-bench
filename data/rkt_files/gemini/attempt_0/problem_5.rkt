#lang racket
(define (solve nums)
  (let loop ([nums nums] [i 1])
    (cond
      [(null? (cdr nums)) (length nums)]
      [(= (car nums) (cadr nums))
       (loop (cdr nums) i)]
      [else (set-car! (vector-ref nums i) (cadr nums))
            (loop (cdr nums) (add1 i)))])))
(print (equal? (solve `(1 1 2)) 2))
(print (equal? (solve `(0 0 1 1 1 2 2 3 3 4)) 5))
(print (equal? (solve `(1 1 1 1)) 1))
(print (equal? (solve `(1 2 3)) 3))
(print (equal? (solve `(1)) 1))
