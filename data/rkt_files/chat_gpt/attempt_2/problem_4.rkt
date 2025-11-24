#lang racket

; Problem: Given a string s with brackets, determine if it is valid.

; Solution:
; Use a closure-based stack to validate the brackets.

(define (solve s)
  (define (make-stack)
    (let ([stack '()])
      (lambda (op . args)
        (cond
          [(equal? op 'push) (set! stack (cons (car args) stack))]
          [(equal? op 'pop) (if (null? stack) #f (let ([top (car stack)]) (set! stack (cdr stack)) top))]
          [(equal? op 'peek) (if (null? stack) #f (car stack))]
          [(equal? op 'is-empty?) (null? stack)]
          [else (error "Unknown operation")]))))
  (define match '((#\) . #\() (#\] . #\[) (#\} . #\{)))
  (define stack (make-stack))
  (let loop ([chars (string->list s)])
    (cond
      [(null? chars) (stack 'is-empty?)]
      [(hash-has-key? match (car chars))
       (if (equal? (stack 'pop) (hash-ref match (car chars)))
           (loop (cdr chars))
           #f)]
      [else (stack 'push (car chars)) (loop (cdr chars))])))

(print (equal? (solve "()") #t))
(print (equal? (solve "()[]{}") #t))
(print (equal? (solve "(]") #f))
(print (equal? (solve "([)]") #f))
(print (equal? (solve "{") #f))
