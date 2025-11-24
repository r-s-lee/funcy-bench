
#lang racket

(define (solve s)
  (let loop ([s s] [stack '()])
    (cond
      [(null? s) (null? stack)]
      [(memq (car s) '(#\( #\{ #\[))
       (loop (cdr s) (cons (car s) stack))]
      [(memq (car s) '(#\) #\} #\]))
       (cond
         [(null? stack) #f]
         [(memq (car stack) `(, (car s)))
          (loop (cdr s) (cdr stack))]
         [else #f])]
      [else #f])))

(print (equal? (solve "()") #t))
(print (equal? (solve "()[]{}") #t))
(print (equal? (solve "(]") #f))
(print (equal? (solve "([)]") #f))
(print (equal? (solve "{") #f))
