#lang racket

; Problem: You are climbing a staircase. Each time you can climb 1 or 2 steps. Return the number of distinct ways to reach the top.

; Solution:
; Use memoization with a recursive function.

(define (solve n)
  (define memo (make-hash))
  (define (ways steps)
    (cond
      [(= steps 0) 1]
      [(< steps 0) 0]
      [(hash-has-key? memo steps) (hash-ref memo steps)]
      [else
       (let ([result (+ (ways (- steps 1)) (ways (- steps 2)))])
         (hash-set! memo steps result)
         result)]))
  (ways n))

(print (equal? (solve 2) 2))
(print (equal? (solve 3) 3))
(print (equal? (solve 5) 8))
(print (equal? (solve 10) 89))
(print (equal? (solve 20) 10946))
