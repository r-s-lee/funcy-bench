#lang racket

; Problem: Climbing Stairs
; Third solution using matrix exponentiation

(define (solve n)
  ; Matrix multiplication for fibonacci-like sequence
  (define (matrix-multiply A B)
    (vector 
     (+ (* (vector-ref A 0) (vector-ref B 0))
        (* (vector-ref A 1) (vector-ref B 2)))
     (+ (* (vector-ref A 0) (vector-ref B 1))
        (* (vector-ref A 1) (vector-ref B 3)))
     (+ (* (vector-ref A 2) (vector-ref B 0))
        (* (vector-ref A 3) (vector-ref B 2)))
     (+ (* (vector-ref A 2) (vector-ref B 1))
        (* (vector-ref A 3) (vector-ref B 3)))))
  
  ; Matrix power function
  (define (matrix-power M k)
    (cond
      [(= k 0) (vector 1 0 0 1)]  ; Identity matrix
      [(= k 1) M]
      [else
       (let* ([half (quotient k 2)]
              [half-power (matrix-power M half)])
         (if (even? k)
             (matrix-multiply half-power half-power)
             (matrix-multiply 
              (matrix-multiply half-power half-power) 
              M)))]))
  
  ; Base cases
  (cond 
    [(<= n 0) 0]
    [(= n 1) 1]
    [(= n 2) 2]
    
    ; Use matrix exponentiation for climbing ways
    [else
     (vector-ref 
      (matrix-power 
       (vector 1 1 1 0)  ; Transformation matrix
       (- n 2)) 
      0)]))
(print (equal? (solve 2) 2))
(print (equal? (solve 3) 3))
(print (equal? (solve 5) 8))
(print (equal? (solve 10) 89))
(print (equal? (solve 20) 10946))
