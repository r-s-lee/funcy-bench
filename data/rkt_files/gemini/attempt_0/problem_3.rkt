#lang racket
(define (solve n)
  (for/list ([i (in-range 1 (add1 n))])
    (cond
      [(zero? (modulo i 15)) "FizzBuzz"]
      [(zero? (modulo i 3)) "Fizz"]
      [(zero? (modulo i 5)) "Buzz"]
      [else (number->string i)])))
(print (equal? (solve 15) `("1" "2" "Fizz" "4" "Buzz" "Fizz" "7" "8" "Fizz" "Buzz" "11" "Fizz" "13" "14" "FizzBuzz")))
(print (equal? (solve 5) `("1" "2" "Fizz" "4" "Buzz")))
(print (equal? (solve 3) `("1" "2" "Fizz")))
(print (equal? (solve 1) `("1")))
(print (equal? (solve 20) `("1" "2" "Fizz" "4" "Buzz" "Fizz" "7" "8" "Fizz" "Buzz" "11" "Fizz" "13" "14" "FizzBuzz" "16" "17" "Fizz" "19" "Buzz")))
