
#lang racket

(define (solve s)
  (let loop ([s s] [depth 0])
    (cond
      [(null? s) (zero? depth)]
      [(memq (car s) '(#\( #\{ #\[))
       (loop (cdr s) (add1 depth))]
      [(memq (car s) '(#\) #\} #\]))
       (if (positive? depth)
           (loop (cdr s) (sub1 depth))
           #f)]
      [else #f])))

(print (equal? (solve "()") #t))
(print (equal? (solve "()[]{}") #t))
(print (equal? (solve "(]") #f))
(print (equal? (solve "([)]") #f))
(print (equal? (solve "{") #f))
