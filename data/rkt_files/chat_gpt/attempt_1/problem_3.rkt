#lang racket

; Problem: Write a program that outputs numbers from 1 to n with 'Fizz', 'Buzz', and 'FizzBuzz' substitutions.

; Solution:
; Generate the sequence by mapping over the range 1 to n.

(define (solve n)
  (map (lambda (i)
         (cond
           [(and (zero? (modulo i 3)) (zero? (modulo i 5))) "FizzBuzz"]
           [(zero? (modulo i 3)) "Fizz"]
           [(zero? (modulo i 5)) "Buzz"]
           [else (number->string i)]))
       (range 1 (add1 n))))

(print (equal? (solve 15) `("1" "2" "Fizz" "4" "Buzz" "Fizz" "7" "8" "Fizz" "Buzz" "11" "Fizz" "13" "14" "FizzBuzz")))
(print (equal? (solve 5) `("1" "2" "Fizz" "4" "Buzz")))
(print (equal? (solve 3) `("1" "2" "Fizz")))
(print (equal? (solve 1) `("1")))
(print (equal? (solve 20) `("1" "2" "Fizz" "4" "Buzz" "Fizz" "7" "8" "Fizz" "Buzz" "11" "Fizz" "13" "14" "FizzBuzz" "16" "17" "Fizz" "19" "Buzz")))
