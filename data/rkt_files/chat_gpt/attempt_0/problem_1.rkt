#lang racket

    ; Problem: Reverse digits of a signed 32-bit integer. Return 0 if the result is out of bounds.

    (define (solve x)
    (define (in-bounds? n) (and (<= -2147483648 n) (<= n 2147483647)))
    (define reversed (string->number
                        (string-append
                        (if (< x 0) "-" "")
                        (string-reverse (number->string (abs x))))))
    (if (in-bounds? reversed) reversed 0))

    
(print (equal? (solve 123) 321))
(print (equal? (solve -123) -321))
(print (equal? (solve 120) 21))
(print (equal? (solve 1534236469) 0))
(print (equal? (solve -2147483648) 0))
