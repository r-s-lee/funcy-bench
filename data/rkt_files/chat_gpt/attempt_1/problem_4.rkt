#lang racket

; Problem: Given a string s with brackets, determine if it is valid.

; Solution:
; Use a recursive helper function to simulate stack-based matching.

(define (solve s)
  (define (validate stack chars)
    (cond
      [(null? chars) (null? stack)]
      [(member (car chars) '(#\) #\] #\}))
       (if (and (not (null? stack))
                (or (and (equal? (car chars) #\)) (equal? (car stack) #\()))
                    (and (equal? (car chars) #\]) (equal? (car stack) #\[))
                    (and (equal? (car chars) #\}) (equal? (car stack) #\{))))
           (validate (cdr stack) (cdr chars))
           #f)]
      [else (validate (cons (car chars) stack) (cdr chars))]))
  (validate '() (string->list s)))

(print (equal? (solve "()") #t))
(print (equal? (solve "()[]{}") #t))
(print (equal? (solve "(]") #f))
(print (equal? (solve "([)]") #f))
(print (equal? (solve "{") #f))
