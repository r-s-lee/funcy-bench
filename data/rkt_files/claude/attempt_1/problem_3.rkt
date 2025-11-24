#lang racket

; Problem: FizzBuzz
; Alternative solution using pattern matching and functional composition

(define (solve n)
  ; Functional composition for FizzBuzz determination
  (define (fizzbuzz-mapper i)
    (match (list (zero? (remainder i 3))
                 (zero? (remainder i 5)))
      [`(#t #t) "FizzBuzz"]
      [`(#t #f) "Fizz"]
      [`(#f #t) "Buzz"]
      [`(#f #f) (number->string i)]))
  
  ; Map over range of numbers
  (map fizzbuzz-mapper (range 1 (add1 n))))
(print (equal? (solve 15) `("1" "2" "Fizz" "4" "Buzz" "Fizz" "7" "8" "Fizz" "Buzz" "11" "Fizz" "13" "14" "FizzBuzz")))
(print (equal? (solve 5) `("1" "2" "Fizz" "4" "Buzz")))
(print (equal? (solve 3) `("1" "2" "Fizz")))
(print (equal? (solve 1) `("1")))
(print (equal? (solve 20) `("1" "2" "Fizz" "4" "Buzz" "Fizz" "7" "8" "Fizz" "Buzz" "11" "Fizz" "13" "14" "FizzBuzz" "16" "17" "Fizz" "19" "Buzz")))
