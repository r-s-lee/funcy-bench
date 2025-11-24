#lang racket

; Problem: Two Sum
; Find indices of two numbers in an array that add up to a target
; Alternative solution using recursion and linear search

(define (solve nums target)
  ; Helper function to find complement recursively
  (define (find-complement lst current-index)
    (cond
      ; Reached end of list without finding solution
      [(null? lst) #f]
      
      ; Check if current number's complement exists in remaining list
      [else
       (define complement (- target (car lst)))
       (define remaining-indices 
         (find-complement-in-rest (cdr lst) complement current-index))
       
       (if remaining-indices
           (list current-index (car remaining-indices))
           (find-complement (cdr lst) (add1 current-index)))]))
  
  ; Search for complement in remaining list
  (define (find-complement-in-rest lst complement start-index)
    (let loop ([rest-lst lst]
               [current-index (add1 start-index)])
      (cond
        [(null? rest-lst) #f]
        [(= (car rest-lst) complement) current-index]
        [else (loop (cdr rest-lst) (add1 current-index))])))
  
  ; Start the search from the beginning of the list
  (find-complement nums 0))
(print (equal? (solve `(2 7 11 15) 9) `(0 1)))
(print (equal? (solve `(3 2 4) 6) `(1 2)))
(print (equal? (solve `(3 3) 6) `(0 1)))
(print (equal? (solve `(1 5 5 3) 10) `(1 2)))
(print (equal? (solve `(0 0 4 -2 2) 2) `(2 3)))
