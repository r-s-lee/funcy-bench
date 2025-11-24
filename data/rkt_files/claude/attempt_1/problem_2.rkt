#lang racket

; Problem: Palindrome Number
; Alternative solution using digit extraction and comparison

(define (solve x)
  ; Immediate rejections
  (cond 
    ; Negative numbers are not palindromes
    [(negative? x) #f]
    
    ; Single-digit numbers are palindromes
    [(< x 10) #t]
    
    ; Numbers ending in 0 (except 0) are not palindromes
    [(and (> x 0) (zero? (remainder x 10))) #f]
    
    [else
     ; Extract digits and compare
     (define (extract-digits n)
       (let loop ([current n]
                  [digits '()])
         (if (zero? current)
             digits
             (loop (quotient current 10) 
                   (cons (remainder current 10) digits)))))
     
     ; Compare extracted digits
     (define digits (extract-digits x))
     (equal? digits (reverse digits))]))
(print (equal? (solve 121) #t))
(print (equal? (solve -121) #f))
(print (equal? (solve 10) #f))
(print (equal? (solve 0) #t))
(print (equal? (solve 1234321) #t))
