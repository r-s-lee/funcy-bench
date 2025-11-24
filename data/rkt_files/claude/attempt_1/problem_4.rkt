#lang racket

; Problem: Valid Parentheses
; Alternative solution using accumulator and functional approach

(define (solve s)
  ; Bracket matching rules
  (define opening-brackets (set #\( #\{ #\[))
  (define closing-brackets (set #\) #\} #\]))
  (define bracket-pairs 
    (hash #\) #\(
          #\} #\{
          #\] #\[))
  
  ; Functional validation with accumulator
  (define (validate-brackets chars)
    (let loop ([remaining chars]
               [stack '()])
      (cond
        ; Successfully processed all characters
        [(and (null? remaining) (null? stack)) #t]
        
        ; Reached end but stack not empty
        [(null? remaining) #f]
        
        ; Opening bracket: push to stack
        [(set-member? opening-brackets (car remaining))
         (loop (cdr remaining) (cons (car remaining) stack))]
        
        ; Closing bracket processing
        [(set-member? closing-brackets (car remaining))
         (cond
           ; Empty stack with closing bracket
           [(null? stack) #f]
           
           ; Mismatched brackets
           [(not (equal? (car stack) 
                         (hash-ref bracket-pairs (car remaining)))) #f]
           
           ; Matched bracket: pop from stack
           [else (loop (cdr remaining) (cdr stack))])]
        
        ; Non-bracket character
        [else (loop (cdr remaining) stack)])))
  
  (validate-brackets (string->list s)))
(print (equal? (solve "()") #t))
(print (equal? (solve "()[]{}") #t))
(print (equal? (solve "(]") #f))
(print (equal? (solve "([)]") #f))
(print (equal? (solve "{") #f))
