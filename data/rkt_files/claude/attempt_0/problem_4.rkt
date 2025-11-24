#lang racket

    ; Problem: Valid Parentheses
    ; Check if parentheses are balanced and correctly nested

    (define (solve s)
    ; Define mapping of closing to opening brackets
    (define bracket-pairs 
        (hash ')' #\( 
            '}' #\{ 
            ']' #\[))
    
    ; Use a stack to track opening brackets
    (define (validate-brackets str)
        (let loop ([chars (string->list str)]
                [stack '()])
        (cond
            ; Successfully processed all characters with empty stack
            [(and (null? chars) (null? stack)) #t]
            
            ; If stack is empty and we have a closing bracket, it's invalid
            [(and (null? stack) 
                (hash-has-key? bracket-pairs (car chars))) #f]
            
            ; Opening bracket: push to stack
            [(not (hash-has-key? bracket-pairs (car chars)))
            (loop (cdr chars) (cons (car chars) stack))]
            
            ; Closing bracket: check if matches top of stack
            [(equal? (car stack) 
                    (hash-ref bracket-pairs (car chars)))
            (loop (cdr chars) (cdr stack))]
            
            ; Mismatched brackets
            [else #f])))
    
    (validate-brackets s))
        
(print (equal? (solve "()") #t))
(print (equal? (solve "()[]{}") #t))
(print (equal? (solve "(]") #f))
(print (equal? (solve "([)]") #f))
(print (equal? (solve "{") #f))
