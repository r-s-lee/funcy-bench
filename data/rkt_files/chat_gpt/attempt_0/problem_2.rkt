#lang racket

    ; Problem: Check if an integer is a palindrome.

    (define (solve x)
    (if (< x 0)
        #f
        (let ([str (number->string x)])
            (string=? str (string-reverse str)))))

    
(print (equal? (solve 121) #t))
(print (equal? (solve -121) #f))
(print (equal? (solve 10) #f))
(print (equal? (solve 0) #t))
(print (equal? (solve 1234321) #t))
