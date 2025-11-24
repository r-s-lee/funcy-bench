#lang racket

; Problem: Write a program that outputs numbers from 1 to n with 'Fizz', 'Buzz', and 'FizzBuzz' substitutions.

; Solution:
; Use a recursive function to generate the sequence.

(define (solve n)
  (define (fizzbuzz i)
    (cond
      [(> i n) '()]
      [(= 0 (modulo i 15)) (cons "FizzBuzz" (fizzbuzz (add1 i)))]
      [(= 0 (modulo i 3)) (cons "Fizz" (fizzbuzz (add1 i)))]
      [(= 0 (modulo i 5)) (cons "Buzz" (fizzbuzz (add1 i)))]
      [else (cons (number->string i) (fizzbuzz (add1 i)))]))
  (fizzbuzz 1))

(print (equal? (solve 15) `("1" "2" "Fizz" "4" "Buzz" "Fizz" "7" "8" "Fizz" "Buzz" "11" "Fizz" "13" "14" "FizzBuzz")))
(print (equal? (solve 5) `("1" "2" "Fizz" "4" "Buzz")))
(print (equal? (solve 3) `("1" "2" "Fizz")))
(print (equal? (solve 1) `("1")))
(print (equal? (solve 20) `("1" "2" "Fizz" "4" "Buzz" "Fizz" "7" "8" "Fizz" "Buzz" "11" "Fizz" "13" "14" "FizzBuzz" "16" "17" "Fizz" "19" "Buzz")))
