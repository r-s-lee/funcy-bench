#lang racket

    ; Problem: Check if a string of brackets is valid.

    (define (solve s)
    (define matching (hash '(' ')' '[' ']' '{' '}'))
    (define stack '())
    (for ([c (in-string s)])
        (if (hash-has-key? matching c)
            (set! stack (cons c stack))
            (if (or (null? stack) (not (= (hash-ref matching (car stack)) c)))
                (return #f)
                (set! stack (cdr stack)))))
    (null? stack))

    
(print (equal? (solve "()") #t))
(print (equal? (solve "()[]{}") #t))
(print (equal? (solve "(]") #f))
(print (equal? (solve "([)]") #f))
(print (equal? (solve "{") #f))
