#lang racket

    ; Problem: Palindrome Number
    ; Determine if an integer reads the same backward as forward

    (define (solve x)
    ; Negative numbers are not palindromes
    (cond 
        ; Negative numbers cannot be palindromes
        [(negative? x) #f]
        
        ; Single-digit numbers are always palindromes
        [(< x 10) #t]
        
        ; Numbers ending in 0 (except 0 itself) are not palindromes
        [(and (> x 0) (zero? (remainder x 10))) #f]
        
        ; Compare original number with its reversed version
        [else 
        (define (reverse-number n)
        (string->number (string-reverse (number->string n))))
        
        (= x (reverse-number x))]))
        
(print (equal? (solve 121) #t))
(print (equal? (solve -121) #f))
(print (equal? (solve 10) #f))
(print (equal? (solve 0) #t))
(print (equal? (solve 1234321) #t))
