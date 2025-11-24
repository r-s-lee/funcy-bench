#lang racket

; Problem: FizzBuzz
; Third solution using stream processing and lazy evaluation

(define (solve n)
  ; Generate FizzBuzz stream
  (define (fizzbuzz-generator)
    (stream-map 
     (lambda (i)
       (cond
         [(and (zero? (remainder i 3)) 
               (zero? (remainder i 5))) "FizzBuzz"]
         [(zero? (remainder i 3)) "Fizz"]
         [(zero? (remainder i 5)) "Buzz"]
         [else (number->string i)]))
     (in-range 1 (add1 n))))
  
  ; Convert stream to list
  (stream->list (fizzbuzz-generator)))
(print (equal? (solve 15) `("1" "2" "Fizz" "4" "Buzz" "Fizz" "7" "8" "Fizz" "Buzz" "11" "Fizz" "13" "14" "FizzBuzz")))
(print (equal? (solve 5) `("1" "2" "Fizz" "4" "Buzz")))
(print (equal? (solve 3) `("1" "2" "Fizz")))
(print (equal? (solve 1) `("1")))
(print (equal? (solve 20) `("1" "2" "Fizz" "4" "Buzz" "Fizz" "7" "8" "Fizz" "Buzz" "11" "Fizz" "13" "14" "FizzBuzz" "16" "17" "Fizz" "19" "Buzz")))
