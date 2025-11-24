#lang racket

    ; Problem: Two Sum
    ; Find indices of two numbers in an array that add up to a target

    (define (solve nums target)
    ; Create a hash table to store complement values and their indices
    (define complement-table (make-hash))
    
    ; Iterate through the list with indices
    (for/first ([num (in-indexed nums)]
                ; Break the iteration when a solution is found
                #:when (or (hash-has-key? complement-table (first num))
                            (hash-set! complement-table (- target (second num)) (first num))))
        (if (hash-has-key? complement-table (second num))
            ; Return indices if complement is found
            (list (hash-ref complement-table (second num)) (first num))
            ; Otherwise continue searching
            #f)))
(print (equal? (solve `(2 7 11 15) 9) `(0 1)))
(print (equal? (solve `(3 2 4) 6) `(1 2)))
(print (equal? (solve `(3 3) 6) `(0 1)))
(print (equal? (solve `(1 5 5 3) 10) `(1 2)))
(print (equal? (solve `(0 0 4 -2 2) 2) `(2 3)))
