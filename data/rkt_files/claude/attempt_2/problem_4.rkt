#lang racket

; Problem: Valid Parentheses
; Third solution using reduction and accumulation

(define (solve s)
  ; Bracket matching rules
  (define bracket-pairs 
    (hash #\) #\(
          #\} #\{
          #\] #\[))
  
  ; Validate using fold/reduce
  (define (validate-brackets chars)
    (define (process-char char acc)
      ; Accumulator is a list: (is-valid? . stack)
      (match acc
        [`(#f . ,_) acc]  ; Already invalid
        [`(#t . ,stack)
         (cond
           ; Opening bracket: push to stack
           [(not (hash-has-key? bracket-pairs char))
            `(#t . ,(cons char stack))]
           
           ; Closing bracket with empty stack
           [(null? stack) `(#f . ,stack)]
           
           ; Mismatched closing bracket
           [(not (equal? (car stack)
                         (hash-ref bracket-pairs char)))
            `(#f . ,stack)]
           
           ; Matched closing bracket
           [else `(#t . ,(cdr stack))])]))
    
    ; Process chars and check final state
    (match (foldl process-char 
                  `(#t . ())  ; Initial state
                  chars)
      [`(#t . ()) #t]  ; Valid and empty stack
      [_ #f]))
  
  (validate-brackets (string->list s)))
(print (equal? (solve "()") #t))
(print (equal? (solve "()[]{}") #t))
(print (equal? (solve "(]") #f))
(print (equal? (solve "([)]") #f))
(print (equal? (solve "{") #f))
