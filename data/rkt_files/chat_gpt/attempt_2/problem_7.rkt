#lang racket

; Problem: Given an integer array nums, find the contiguous subarray with the largest sum and return its sum.

; Solution:
; Use a divide-and-conquer approach to calculate the maximum sum.

(define (solve nums)
  (define (max-crossing-sum arr low mid high)
    (let loop-left ([i mid] [sum 0] [left-sum -inf])
      (if (< i low)
          left-sum
          (let ([sum (+ sum (list-ref arr i))])
            (loop-left (- i 1) sum (max left-sum sum)))))
    (let loop-right ([i (+ mid 1)] [sum 0] [right-sum -inf])
      (if (> i high)
          right-sum
          (let ([sum (+ sum (list-ref arr i))])
            (loop-right (+ i 1) sum (max right-sum sum)))))
    (+ left-sum right-sum))
  
  (define (max-subarray arr low high)
    (if (= low high)
        (list-ref arr low)
        (let ([mid (quotient (+ low high) 2)])
          (max (max-subarray arr low mid)
               (max-subarray arr (+ mid 1) high)
               (max-crossing-sum arr low mid high)))))
  
  (max-subarray nums 0 (- (length nums) 1)))

(print (equal? (solve `(-2 1 -3 4 -1 2 1 -5 4)) 6))
(print (equal? (solve `(1)) 1))
(print (equal? (solve `(5 4 -1 7 8)) 23))
(print (equal? (solve `(-1 -2 -3)) -1))
(print (equal? (solve `(10 -1 -1 10)) 18))
