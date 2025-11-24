#lang racket

    ; Problem: Merge two sorted linked lists.

    (define (solve l1 l2)
    (cond
        [(null? l1) l2]
        [(null? l2) l1]
        [(<= (car l1) (car l2))
        (cons (car l1) (merge-two-lists (cdr l1) l2))]
        [else
        (cons (car l2) (merge-two-lists l1 (cdr l2)))]))

    
(print (equal? (solve `(1 1 2)) 2))
(print (equal? (solve `(0 0 1 1 1 2 2 3 3 4)) 5))
(print (equal? (solve `(1 1 1 1)) 1))
(print (equal? (solve `(1 2 3)) 3))
(print (equal? (solve `(1)) 1))
