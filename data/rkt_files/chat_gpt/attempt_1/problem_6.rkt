#lang racket

; Problem: You are climbing a staircase. Each time you can climb 1 or 2 steps. Return the number of distinct ways to reach the top.

; Solution:
; Use a bottom-up dynamic programming approach with O(1) space.

(define (solve n)
  (cond
    [(= n 1) 1]
    [(= n 2) 2]
    [else
     (let loop ([prev2 1] [prev1 2] [i 3])
       (if (> i n)
           prev1
           (loop prev1 (+ prev1 prev2) (add1 i))))]))

(print (equal? (solve 2) 2))
(print (equal? (solve 3) 3))
(print (equal? (solve 5) 8))
(print (equal? (solve 10) 89))
(print (equal? (solve 20) 10946))
