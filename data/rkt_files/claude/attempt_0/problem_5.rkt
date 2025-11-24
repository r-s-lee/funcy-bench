#lang racket

    ; Problem: Remove Duplicates from Sorted Array
    ; Remove duplicates in-place and return new length

    (define (solve nums)
    ; If list is empty, return 0
    (if (null? nums)
        0
        ; Use foldl to track unique elements and their count
        (let loop ([nums nums]
                    [unique-list '()]
                    [unique-count 0])
            (cond 
            ; Empty list, return count of unique elements
            [(null? nums) unique-count]
            
            ; First element or different from last unique
            [(or (null? unique-list)
                (not (= (car nums) (car unique-list))))
            (loop (cdr nums) 
                    (cons (car nums) unique-list)
                    (add1 unique-count))]
            
            ; Duplicate found, skip
            [else 
            (loop (cdr nums) 
                    unique-list 
                    unique-count)]))))
        
(print (equal? (solve `(1 1 2)) 2))
(print (equal? (solve `(0 0 1 1 1 2 2 3 3 4)) 5))
(print (equal? (solve `(1 1 1 1)) 1))
(print (equal? (solve `(1 2 3)) 3))
(print (equal? (solve `(1)) 1))
