#lang racket

; Problem: Remove Duplicates from Sorted Array
; Third solution using folding and custom accumulation

(define (solve nums)
  ; Custom fold to track unique elements
  (define (count-unique lst)
    (first 
     (foldl 
      (lambda (current acc)
        (define last-unique (first acc))
        (define count (second acc))
        
        ; First element or different from last unique
        (if (or (null? last-unique) 
                (not (= current (car last-unique))))
            (list (cons current last-unique) (add1 count))
            acc))
      (list '() 0)
      lst)))
  
  (count-unique nums))
(print (equal? (solve `(1 1 2)) 2))
(print (equal? (solve `(0 0 1 1 1 2 2 3 3 4)) 5))
(print (equal? (solve `(1 1 1 1)) 1))
(print (equal? (solve `(1 2 3)) 3))
(print (equal? (solve `(1)) 1))
