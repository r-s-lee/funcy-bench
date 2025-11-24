#lang racket

; Problem: Maximum Subarray
; Third solution using divide and conquer approach

(define (solve nums)
  ; Divide and conquer max subarray sum
  (define (max-crossing-sum arr low mid high)
    (define left-sum 
      (let loop ([i mid]
                 [sum 0]
                 [max-sum (- (expt 2 31))])
        (if (< i low)
            max-sum
            (let* ([new-sum (+ sum (list-ref arr i))]
                   [new-max (max max-sum new-sum)])
              (loop (sub1 i) new-sum new-max)))))
    
    (define right-sum
      (let loop ([i (add1 mid)]
                 [sum 0]
                 [max-sum (- (expt 2 31))])
        (if (> i high)
            max-sum
            (let* ([new-sum (+ sum (list-ref arr i))]
                   [new-max (max max-sum new-sum)])
              (loop (add1 i) new-sum new-max)))))
    
    (+ left-sum right-sum))
  
  ; Recursive max subarray function
  (define (max-subarray-sum arr low high)
    ; Base case: single element
    (if (= low high)
        (list-ref arr low)
        
        ; Divide
        (let* ([mid (quotient (+ low high) 2)]
               [left-sum (max-subarray-sum arr low mid)]
               [right-sum (max-subarray-sum arr (add1 mid) high)]
               [cross-sum (max-crossing-sum arr low mid high)])
          
          ; Conquer: find maximum of three possibilities
          (max left-sum right-sum cross-sum))))
  
  ; Invoke divide and conquer
  (max-subarray-sum nums 0 (sub1 (length nums))))
(print (equal? (solve `(-2 1 -3 4 -1 2 1 -5 4)) 6))
(print (equal? (solve `(1)) 1))
(print (equal? (solve `(5 4 -1 7 8)) 23))
(print (equal? (solve `(-1 -2 -3)) -1))
(print (equal? (solve `(10 -1 -1 10)) 18))
