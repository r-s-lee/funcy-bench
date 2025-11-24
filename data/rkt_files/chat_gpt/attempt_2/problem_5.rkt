#lang racket

; Problem: Given an array of integers nums, remove duplicates in-place such that each element appears only once and return the new length.

; Solution:
; Use a pointer to track unique elements and overwrite duplicates.

(define (solve nums)
  (if (null? nums)
      0
      (let loop ([write-index 1] [read-index 1])
        (if (>= read-index (length nums))
            write-index
            (begin
              (if (not (= (list-ref nums read-index) (list-ref nums (- read-index 1))))
                  (begin
                    (vector-set! nums write-index (list-ref nums read-index))
                    (set! write-index (add1 write-index))))
              (loop write-index (add1 read-index)))))))

(print (equal? (solve `(1 1 2)) 2))
(print (equal? (solve `(0 0 1 1 1 2 2 3 3 4)) 5))
(print (equal? (solve `(1 1 1 1)) 1))
(print (equal? (solve `(1 2 3)) 3))
(print (equal? (solve `(1)) 1))
