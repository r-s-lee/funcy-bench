#lang racket

; Problem: Reverse Integer
; Third solution using string manipulation and custom parsing

(define (solve x)
  ; Convert integer to string, handle sign separately
  (define str-num 
    (string-trim 
     (number->string (abs x)) 
     #:left? #t 
     #:right? #t))
  
  ; Reverse string and convert back to integer
  (define reversed-str 
    (list->string 
     (reverse (string->list str-num))))
  
  ; Parse reversed string, apply original sign
  (define result
    (* (if (negative? x) -1 1)
       (string->number reversed-str)))
  
  ; 32-bit integer overflow check
  (if (or (< result (- (expt 2 31))) 
          (>= result (expt 2 31)))
      0
      result))
(print (equal? (solve 123) 321))
(print (equal? (solve -123) -321))
(print (equal? (solve 120) 21))
(print (equal? (solve 1534236469) 0))
(print (equal? (solve -2147483648) 0))
