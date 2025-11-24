
#lang racket

(define (solve nums target)
  (for/list ([i (in-range (length nums))])
    (let ([complement (- target (vector-ref nums i))])
      (for/list ([j (in-range (add1 i) (length nums))])
        (when (= complement (vector-ref nums j))
          (return (list i j)))))))
  #f)

(print (equal? (solve `(2 7 11 15) 9) `(0 1)))
(print (equal? (solve `(3 2 4) 6) `(1 2)))
(print (equal? (solve `(3 3) 6) `(0 1)))
(print (equal? (solve `(1 5 5 3) 10) `(1 2)))
(print (equal? (solve `(0 0 4 -2 2) 2) `(2 3)))
