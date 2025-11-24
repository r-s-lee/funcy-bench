#lang racket

    ; Problem: Reverse Integer
    ; Reverse digits of a signed 32-bit integer while handling overflow

    (define (solve x)
    ; Determine sign of input
    (define sign (if (negative? x) -1 1))
    
    ; Convert to positive number for processing
    (define abs-x (abs x))
    
    ; Convert integer to string, reverse it, convert back to integer
    (define reversed 
        (string->number 
        (string-reverse 
        (number->string abs-x))))
    
    ; Apply sign and check 32-bit integer constraints
    (define result (* sign reversed))
    
    ; Return 0 if result is outside 32-bit signed integer range
    (if (or (< result (- (expt 2 31))) 
            (>= result (expt 2 31)))
        0
        result))
        
(print (equal? (solve 123) 321))
(print (equal? (solve -123) -321))
(print (equal? (solve 120) 21))
(print (equal? (solve 1534236469) 0))
(print (equal? (solve -2147483648) 0))
