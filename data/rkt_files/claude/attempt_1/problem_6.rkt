#lang racket

; Problem: Climbing Stairs
; Alternative solution using tail recursion and memoization

(define (solve n)
  ; Memoized climbing ways computation
  (define memo (make-hash))
  
  ; Tail-recursive helper function
  (define (climb-stairs-memo k)
    (cond
      [(<= k 0) 0]
      [(= k 1) 1]
      [(= k 2) 2]
      ; Check memoized result
      [(hash-has-key? memo k) (hash-ref memo k)]
      [else
       ; Compute and memoize
       (define result 
         (+ (climb-stairs-memo (- k 1))
            (climb-stairs-memo (- k 2))))
       (hash-set! memo k result)
       result]))
  
  (climb-stairs-memo n))
(print (equal? (solve 2) 2))
(print (equal? (solve 3) 3))
(print (equal? (solve 5) 8))
(print (equal? (solve 10) 89))
(print (equal? (solve 20) 10946))
