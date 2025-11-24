#lang racket

; Problem: Palindrome Number
; Third solution using mathematical approach without string conversion

(define (solve x)
  ; Immediate rejections
  (cond 
    [(negative? x) #f]
    [(< x 10) #t]
    [(and (> x 0) (zero? (remainder x 10))) #f]
    
    [else
     ; Mathematically reverse the number
     (define (reverse-number n)
       (let loop ([original n]
                  [reversed 0])
         (if (zero? original)
             reversed
             (let* ([digit (remainder original 10)]
                    [new-reversed (+ (* reversed 10) digit)])
               (loop (quotient original 10) new-reversed)))))
     
     ; Compare original with reversed
     (= x (reverse-number x))]))
(print (equal? (solve 121) #t))
(print (equal? (solve -121) #f))
(print (equal? (solve 10) #f))
(print (equal? (solve 0) #t))
(print (equal? (solve 1234321) #t))
