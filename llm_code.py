llm_generated_code = {
    "chat_gpt": 
        [["""#lang racket

    ; Problem: Return indices of two numbers in an array such that they add up to a given target.

    (define (solve nums target)
    (define ht (make-hash))
    (for ([i (in-range (length nums))])
        (let ([complement (- target (list-ref nums i))])
        (if (hash-has-key? ht complement)
            (list (hash-ref ht complement) i)
            (hash-set! ht (list-ref nums i) i)))))

    """,
    """#lang racket

    ; Problem: Reverse digits of a signed 32-bit integer. Return 0 if the result is out of bounds.

    (define (solve x)
    (define (in-bounds? n) (and (<= -2147483648 n) (<= n 2147483647)))
    (define reversed (string->number
                        (string-append
                        (if (< x 0) "-" "")
                        (string-reverse (number->string (abs x))))))
    (if (in-bounds? reversed) reversed 0))

    """,
    """#lang racket

    ; Problem: Check if an integer is a palindrome.

    (define (solve x)
    (if (< x 0)
        #f
        (let ([str (number->string x)])
            (string=? str (string-reverse str)))))

    """,
    """#lang racket

    ; Problem: Return a FizzBuzz sequence from 1 to n.

    (define (solve n)
    (for/list ([i (in-range 1 (+ n 1))])
        (cond
        [(= 0 (modulo i 15)) "FizzBuzz"]
        [(= 0 (modulo i 3)) "Fizz"]
        [(= 0 (modulo i 5)) "Buzz"]
        [else (number->string i)])))

    """,
    """#lang racket

    ; Problem: Check if a string of brackets is valid.

    (define (solve s)
    (define matching (hash '(' ')' '[' ']' '{' '}'))
    (define stack '())
    (for ([c (in-string s)])
        (if (hash-has-key? matching c)
            (set! stack (cons c stack))
            (if (or (null? stack) (not (= (hash-ref matching (car stack)) c)))
                (return #f)
                (set! stack (cdr stack)))))
    (null? stack))

    """,
    """#lang racket

    ; Problem: Merge two sorted linked lists.

    (define (solve l1 l2)
    (cond
        [(null? l1) l2]
        [(null? l2) l1]
        [(<= (car l1) (car l2))
        (cons (car l1) (merge-two-lists (cdr l1) l2))]
        [else
        (cons (car l2) (merge-two-lists l1 (cdr l2)))]))

    """,
    """#lang racket

    ; Problem: Remove duplicates from a sorted array in-place and return the new length.

    (define (solve nums)
    (define n (length nums))
    (if (= n 0)
        0
        (let loop ([i 1] [last 0])
            (if (< i n)
                (if (= (list-ref nums last) (list-ref nums i))
                    (loop (+ i 1) last)
                    (begin
                    (set! nums (+ last 1) (list-ref nums i))
                    (loop (+ i 1) (+ last 1))))
                (+ last 1)))))

    """,
    """#lang racket

    ; Problem: Count distinct ways to climb a staircase of n steps.

    (define (solve n)
    (define dp (make-vector (+ n 1) 0))
    (vector-set! dp 1 1)
    (if (>= n 2) (vector-set! dp 2 2))
    (for ([i (in-range 3 (+ n 1))])
        (vector-set! dp i (+ (vector-ref dp (- i 1)) (vector-ref dp (- i 2)))))
    (vector-ref dp n))

    """,
    """#lang racket

    ; Problem: Find the largest sum of a contiguous subarray.

    (define (solve nums)
    (let loop ([current-max (list-ref nums 0)]
                [global-max (list-ref nums 0)]
                [i 1])
        (if (= i (length nums))
            global-max
            (let ([current (list-ref nums i)])
            (loop (max current (+ current current-max))
                    (max global-max (max current (+ current current-max)))
                    (+ i 1))))))

    """,
    """#lang racket

    ; Problem: Perform inorder traversal of a binary tree.

    (define (solve root)
    (define result '())
    (define (helper node)
        (when node
        (helper (car node)) ; left
        (set! result (append result (list (cadr node)))) ; value
        (helper (caddr node)))) ; right
    (helper root)
    result)

    """
    ], [
"""#lang racket

; Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

; Solution:
; Iterate through the list with nested loops to check every pair of indices.

(define (solve nums target)
  (for*/first ([i (in-range (length nums))]
               [j (in-range (add1 i) (length nums))]
               #:when (= (+ (list-ref nums i) (list-ref nums j)) target))
    (list i j)))
""",
"""#lang racket

; Problem: Given a signed 32-bit integer x, return x with its digits reversed.

; Solution:
; Convert the number to a string, reverse the digits, and check bounds.

(define (solve x)
  (define reversed (string->number (string-reverse (number->string (abs x)))))
  (if (< x 0)
      (set! reversed (- reversed)))
  (if (<= -2147483648 reversed 2147483647)
      reversed
      0))
""",
"""#lang racket

; Problem: Given an integer x, return true if x is a palindrome.

; Solution:
; Compare the number with its reverse without converting to a string.

(define (solve x)
  (if (< x 0)
      #f
      (let loop ([original x] [reversed 0])
        (if (= original 0)
            (= x reversed)
            (loop (quotient original 10)
                  (+ (* reversed 10) (remainder original 10)))))))
""",
"""#lang racket

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
""",
"""#lang racket

; Problem: Given a string s with brackets, determine if it is valid.

; Solution:
; Use a recursive helper function to simulate stack-based matching.

(define (solve s)
  (define (validate stack chars)
    (cond
      [(null? chars) (null? stack)]
      [(member (car chars) '(#\) #\] #\}))
       (if (and (not (null? stack))
                (or (and (equal? (car chars) #\)) (equal? (car stack) #\()))
                    (and (equal? (car chars) #\]) (equal? (car stack) #\[))
                    (and (equal? (car chars) #\}) (equal? (car stack) #\{))))
           (validate (cdr stack) (cdr chars))
           #f)]
      [else (validate (cons (car chars) stack) (cdr chars))]))
  (validate '() (string->list s)))
""", """#lang racket

; Problem: Given an array of integers nums, remove duplicates in-place such that each element appears only once and return the new length.

; Solution:
; Traverse the array, maintaining a pointer for the unique elements.

(define (solve nums)
  (define unique-count 0)
  (for ([i (in-range (length nums))])
    (when (or (= i 0) (not (= (list-ref nums i) (list-ref nums (- i 1)))))
      (set! nums (vector-set! nums unique-count (list-ref nums i)))
      (set! unique-count (add1 unique-count))))
  unique-count)
""",
"""#lang racket

; Problem: You are climbing a staircase. Each time you can climb 1 or 2 steps. Return the number of distinct ways to reach the top.

; Solution:
; Use a bottom-up dynamic programming approach with O(1) space.

(define (solve n)
  (cond
    [(= n 1) 1]
    [(= n 2) 2]
    [else
     (let loop ([prev2 1] [prev1 2] [i 3])
       (if (> i n)
           prev1
           (loop prev1 (+ prev1 prev2) (add1 i))))]))
""",
"""#lang racket

; Problem: Given an integer array nums, find the contiguous subarray with the largest sum and return its sum.

; Solution:
; Use Kadane's algorithm for O(n) time complexity.

(define (solve nums)
  (let loop ([current-max (list-ref nums 0)]
             [global-max (list-ref nums 0)]
             [i 1])
    (if (>= i (length nums))
        global-max
        (let ([new-current-max (max (list-ref nums i) (+ current-max (list-ref nums i)))])
          (loop new-current-max (max global-max new-current-max) (add1 i))))))
"""
], [
"""#lang racket

; Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

; Solution:
; Use recursion to search for the solution.

(define (solve nums target)
  (define (find-pair i)
    (if (= i (length nums))
        '()
        (let loop ([j (add1 i)])
          (cond
            [(= j (length nums)) (find-pair (add1 i))]
            [(= (+ (list-ref nums i) (list-ref nums j)) target) (list i j)]
            [else (loop (add1 j))]))))
  (find-pair 0))
""",
"""#lang racket

; Problem: Given a signed 32-bit integer x, return x with its digits reversed.

; Solution:
; Convert the number to a list of digits, reverse it, and rebuild the number.

(define (solve x)
  (define (number->digits n)
    (if (= n 0)
        '()
        (cons (remainder n 10) (number->digits (quotient n 10)))))
  (define (digits->number digits)
    (foldl (lambda (digit acc) (+ (* acc 10) digit)) 0 digits))
  (let ([reversed (digits->number (reverse (number->digits (abs x))))])
    (if (or (< reversed -2147483648) (> reversed 2147483647))
        0
        (if (< x 0) (- reversed) reversed))))
""",
"""#lang racket

; Problem: Given an integer x, return true if x is a palindrome.

; Solution:
; Use two pointers to compare digits from the front and back.

(define (solve x)
  (define digits (number->string x))
  (let loop ([start 0] [end (- (string-length digits) 1)])
    (cond
      [(>= start end) #t]
      [(not (char=? (string-ref digits start) (string-ref digits end))) #f]
      [else (loop (add1 start) (sub1 end))])))
""",
"""#lang racket

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
""",
"""#lang racket

; Problem: Given a string s with brackets, determine if it is valid.

; Solution:
; Use a closure-based stack to validate the brackets.

(define (solve s)
  (define (make-stack)
    (let ([stack '()])
      (lambda (op . args)
        (cond
          [(equal? op 'push) (set! stack (cons (car args) stack))]
          [(equal? op 'pop) (if (null? stack) #f (let ([top (car stack)]) (set! stack (cdr stack)) top))]
          [(equal? op 'peek) (if (null? stack) #f (car stack))]
          [(equal? op 'is-empty?) (null? stack)]
          [else (error "Unknown operation")]))))
  (define match '((#\) . #\() (#\] . #\[) (#\} . #\{)))
  (define stack (make-stack))
  (let loop ([chars (string->list s)])
    (cond
      [(null? chars) (stack 'is-empty?)]
      [(hash-has-key? match (car chars))
       (if (equal? (stack 'pop) (hash-ref match (car chars)))
           (loop (cdr chars))
           #f)]
      [else (stack 'push (car chars)) (loop (cdr chars))])))
""",
"""#lang racket

; Problem: Given an array of integers nums, remove duplicates in-place such that each element appears only once and return the new length.

; Solution:
; Use a pointer to track unique elements and overwrite duplicates.

(define (solve nums)
  (if (null? nums)
      0
      (let loop ([write-index 1] [read-index 1])
        (if (>= read-index (length nums))
            write-index
            (begin
              (if (not (= (list-ref nums read-index) (list-ref nums (- read-index 1))))
                  (begin
                    (vector-set! nums write-index (list-ref nums read-index))
                    (set! write-index (add1 write-index))))
              (loop write-index (add1 read-index)))))))
""",
"""#lang racket

; Problem: You are climbing a staircase. Each time you can climb 1 or 2 steps. Return the number of distinct ways to reach the top.

; Solution:
; Use memoization with a recursive function.

(define (solve n)
  (define memo (make-hash))
  (define (ways steps)
    (cond
      [(= steps 0) 1]
      [(< steps 0) 0]
      [(hash-has-key? memo steps) (hash-ref memo steps)]
      [else
       (let ([result (+ (ways (- steps 1)) (ways (- steps 2)))])
         (hash-set! memo steps result)
         result)]))
  (ways n))
""",
"""#lang racket

; Problem: Given an integer array nums, find the contiguous subarray with the largest sum and return its sum.

; Solution:
; Use a divide-and-conquer approach to calculate the maximum sum.

(define (solve nums)
  (define (max-crossing-sum arr low mid high)
    (let loop-left ([i mid] [sum 0] [left-sum -inf])
      (if (< i low)
          left-sum
          (let ([sum (+ sum (list-ref arr i))])
            (loop-left (- i 1) sum (max left-sum sum)))))
    (let loop-right ([i (+ mid 1)] [sum 0] [right-sum -inf])
      (if (> i high)
          right-sum
          (let ([sum (+ sum (list-ref arr i))])
            (loop-right (+ i 1) sum (max right-sum sum)))))
    (+ left-sum right-sum))
  
  (define (max-subarray arr low high)
    (if (= low high)
        (list-ref arr low)
        (let ([mid (quotient (+ low high) 2)])
          (max (max-subarray arr low mid)
               (max-subarray arr (+ mid 1) high)
               (max-crossing-sum arr low mid high)))))
  
  (max-subarray nums 0 (- (length nums) 1)))
"""
]
         ], "claude": [[
        '''#lang racket

    ; Problem: Two Sum
    ; Find indices of two numbers in an array that add up to a target

    (define (solve nums target)
    ; Create a hash table to store complement values and their indices
    (define complement-table (make-hash))
    
    ; Iterate through the list with indices
    (for/first ([num (in-indexed nums)]
                ; Break the iteration when a solution is found
                #:when (or (hash-has-key? complement-table (first num))
                            (hash-set! complement-table (- target (second num)) (first num))))
        (if (hash-has-key? complement-table (second num))
            ; Return indices if complement is found
            (list (hash-ref complement-table (second num)) (first num))
            ; Otherwise continue searching
            #f)))''',
        '''#lang racket

    ; Problem: Reverse Integer
    ; Reverse digits of a signed 32-bit integer while handling overflow

    (define (solve x)
    ; Determine sign of input
    (define sign (if (negative? x) -1 1))
    
    ; Convert to positive number for processing
    (define abs-x (abs x))
    
    ; Convert integer to string, reverse it, convert back to integer
    (define reversed 
        (string->number 
        (string-reverse 
        (number->string abs-x))))
    
    ; Apply sign and check 32-bit integer constraints
    (define result (* sign reversed))
    
    ; Return 0 if result is outside 32-bit signed integer range
    (if (or (< result (- (expt 2 31))) 
            (>= result (expt 2 31)))
        0
        result))
        ''',
        '''#lang racket

    ; Problem: Palindrome Number
    ; Determine if an integer reads the same backward as forward

    (define (solve x)
    ; Negative numbers are not palindromes
    (cond 
        ; Negative numbers cannot be palindromes
        [(negative? x) #f]
        
        ; Single-digit numbers are always palindromes
        [(< x 10) #t]
        
        ; Numbers ending in 0 (except 0 itself) are not palindromes
        [(and (> x 0) (zero? (remainder x 10))) #f]
        
        ; Compare original number with its reversed version
        [else 
        (define (reverse-number n)
        (string->number (string-reverse (number->string n))))
        
        (= x (reverse-number x))]))
        ''',
        '''#lang racket

    ; Problem: FizzBuzz
    ; Generate string representations with special rules for multiples

    (define (solve n)
    (for/list ([i (in-range 1 (add1 n))])
        (cond
        [(and (zero? (remainder i 3)) 
                (zero? (remainder i 5))) "FizzBuzz"]
        [(zero? (remainder i 3)) "Fizz"]
        [(zero? (remainder i 5)) "Buzz"]
        [else (number->string i)])))
        ''',
        '''#lang racket

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
        ''',
        '''#lang racket

    ; Problem: Remove Duplicates from Sorted Array
    ; Remove duplicates in-place and return new length

    (define (solve nums)
    ; If list is empty, return 0
    (if (null? nums)
        0
        ; Use foldl to track unique elements and their count
        (let loop ([nums nums]
                    [unique-list '()]
                    [unique-count 0])
            (cond 
            ; Empty list, return count of unique elements
            [(null? nums) unique-count]
            
            ; First element or different from last unique
            [(or (null? unique-list)
                (not (= (car nums) (car unique-list))))
            (loop (cdr nums) 
                    (cons (car nums) unique-list)
                    (add1 unique-count))]
            
            ; Duplicate found, skip
            [else 
            (loop (cdr nums) 
                    unique-list 
                    unique-count)]))))
        ''',
        '''#lang racket

    ; Problem: Climbing Stairs
    ; Count distinct ways to climb n stairs with 1 or 2 steps

    (define (solve n)
    ; Base cases for 0 and 1 steps
    (cond 
        [(<= n 0) 0]
        [(= n 1) 1]
        [(= n 2) 2]
        
        ; Dynamic programming approach
        [else
        (let* ([dp (make-vector (+ n 1) 0)])
        ; Initialize first two steps
        (vector-set! dp 1 1)
        (vector-set! dp 2 2)
        
        ; Compute ways for remaining steps
        (for ([i (in-range 3 (add1 n))])
            (vector-set! dp i 
                        (+ (vector-ref dp (- i 1))
                            (vector-ref dp (- i 2)))))
        
        ; Return total ways
        (vector-ref dp n))]))
        ''',
        '''#lang racket

    ; Problem: Maximum Subarray
    ; Find contiguous subarray with largest sum using Kadane's algorithm

    (define (solve nums)
    ; Kadane's algorithm for maximum subarray sum
    (let loop ([max-sum (car nums)]
                [current-sum (car nums)]
                [rest (cdr nums)])
        (if (null? rest)
            max-sum
            (let* ([next-num (car rest)]
                [new-current (max next-num (+ current-sum next-num))]
                [new-max (max max-sum new-current)])
            (loop new-max new-current (cdr rest))))))'''],
    [
        '''#lang racket

; Problem: Two Sum
; Find indices of two numbers in an array that add up to a target
; Alternative solution using recursion and linear search

(define (solve nums target)
  ; Helper function to find complement recursively
  (define (find-complement lst current-index)
    (cond
      ; Reached end of list without finding solution
      [(null? lst) #f]
      
      ; Check if current number's complement exists in remaining list
      [else
       (define complement (- target (car lst)))
       (define remaining-indices 
         (find-complement-in-rest (cdr lst) complement current-index))
       
       (if remaining-indices
           (list current-index (car remaining-indices))
           (find-complement (cdr lst) (add1 current-index)))]))
  
  ; Search for complement in remaining list
  (define (find-complement-in-rest lst complement start-index)
    (let loop ([rest-lst lst]
               [current-index (add1 start-index)])
      (cond
        [(null? rest-lst) #f]
        [(= (car rest-lst) complement) current-index]
        [else (loop (cdr rest-lst) (add1 current-index))])))
  
  ; Start the search from the beginning of the list
  (find-complement nums 0))''',
  '''#lang racket

; Problem: Reverse Integer
; Alternative solution using explicit digit manipulation

(define (solve x)
  ; Handle sign separately
  (define sign (if (negative? x) -1 1))
  (define abs-x (abs x))
  
  ; Recursive digit reversal
  (define (reverse-digits n)
    (let reverse-loop ([current n]
                       [reversed 0])
      (if (zero? current)
          reversed
          (let* ([digit (remainder current 10)]
                 [new-reversed (+ (* reversed 10) digit)])
            (reverse-loop (quotient current 10) new-reversed)))))
  
  ; Compute reversed number and apply sign
  (define result (* sign (reverse-digits abs-x)))
  
  ; Check 32-bit integer constraints
  (if (or (< result (- (expt 2 31))) 
          (>= result (expt 2 31)))
      0
      result))''',
      '''#lang racket

; Problem: Palindrome Number
; Alternative solution using digit extraction and comparison

(define (solve x)
  ; Immediate rejections
  (cond 
    ; Negative numbers are not palindromes
    [(negative? x) #f]
    
    ; Single-digit numbers are palindromes
    [(< x 10) #t]
    
    ; Numbers ending in 0 (except 0) are not palindromes
    [(and (> x 0) (zero? (remainder x 10))) #f]
    
    [else
     ; Extract digits and compare
     (define (extract-digits n)
       (let loop ([current n]
                  [digits '()])
         (if (zero? current)
             digits
             (loop (quotient current 10) 
                   (cons (remainder current 10) digits)))))
     
     ; Compare extracted digits
     (define digits (extract-digits x))
     (equal? digits (reverse digits))]))''',
     '''#lang racket

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
  (map fizzbuzz-mapper (range 1 (add1 n))))''',
  '''#lang racket

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
  
  (validate-brackets (string->list s)))''',
  '''#lang racket

; Problem: Remove Duplicates from Sorted Array
; Alternative solution using set operations and functional approach

(define (solve nums)
  ; Use set to track unique elements efficiently
  (define unique-set (apply set nums))
  
  ; Convert set back to sorted list and count
  (set-count unique-set))''',
  '''#lang racket

; Problem: Climbing Stairs
; Alternative solution using tail recursion and memoization

(define (solve n)
  ; Memoized climbing ways computation
  (define memo (make-hash))
  
  ; Tail-recursive helper function
  (define (climb-stairs-memo k)
    (cond
      [(<= k 0) 0]
      [(= k 1) 1]
      [(= k 2) 2]
      ; Check memoized result
      [(hash-has-key? memo k) (hash-ref memo k)]
      [else
       ; Compute and memoize
       (define result 
         (+ (climb-stairs-memo (- k 1))
            (climb-stairs-memo (- k 2))))
       (hash-set! memo k result)
       result]))
  
  (climb-stairs-memo n))''',
  '''#lang racket

; Problem: Maximum Subarray
; Alternative solution using functional folding approach

(define (solve nums)
  ; Functional fold to compute maximum subarray sum
  (first 
   (foldl 
    (lambda (current-num acc)
      (define current-sum (first acc))
      (define max-sum (second acc))
      (define new-sum (max current-num (+ current-sum current-num)))
      (define new-max (max max-sum new-sum))
      (list new-sum new-max))
    (list (car nums) (car nums))
    (cdr nums))))'''
    ], [
        '''#lang racket

; Problem: Two Sum
; Third solution using higher-order functions and generator-like approach

(define (solve nums target)
  ; Generate all possible index pairs
  (define (generate-index-pairs nums)
    (for*/first ([i (in-range (length nums))]
                 [j (in-range (add1 i) (length nums))]
                 #:when (= (+ (list-ref nums i) 
                              (list-ref nums j)) 
                           target))
      (list i j)))
  
  (generate-index-pairs nums))''',
  '''#lang racket

; Problem: Reverse Integer
; Third solution using string manipulation and custom parsing

(define (solve x)
  ; Convert integer to string, handle sign separately
  (define str-num 
    (string-trim 
     (number->string (abs x)) 
     #:left? #t 
     #:right? #t))
  
  ; Reverse string and convert back to integer
  (define reversed-str 
    (list->string 
     (reverse (string->list str-num))))
  
  ; Parse reversed string, apply original sign
  (define result
    (* (if (negative? x) -1 1)
       (string->number reversed-str)))
  
  ; 32-bit integer overflow check
  (if (or (< result (- (expt 2 31))) 
          (>= result (expt 2 31)))
      0
      result))''',
      '''#lang racket

; Problem: Palindrome Number
; Third solution using mathematical approach without string conversion

(define (solve x)
  ; Immediate rejections
  (cond 
    [(negative? x) #f]
    [(< x 10) #t]
    [(and (> x 0) (zero? (remainder x 10))) #f]
    
    [else
     ; Mathematically reverse the number
     (define (reverse-number n)
       (let loop ([original n]
                  [reversed 0])
         (if (zero? original)
             reversed
             (let* ([digit (remainder original 10)]
                    [new-reversed (+ (* reversed 10) digit)])
               (loop (quotient original 10) new-reversed)))))
     
     ; Compare original with reversed
     (= x (reverse-number x))]))''',
     '''#lang racket

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
  (stream->list (fizzbuzz-generator)))''',
  '''#lang racket

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
  
  (validate-brackets (string->list s)))''',
  '''#lang racket

; Problem: Remove Duplicates from Sorted Array
; Third solution using folding and custom accumulation

(define (solve nums)
  ; Custom fold to track unique elements
  (define (count-unique lst)
    (first 
     (foldl 
      (lambda (current acc)
        (define last-unique (first acc))
        (define count (second acc))
        
        ; First element or different from last unique
        (if (or (null? last-unique) 
                (not (= current (car last-unique))))
            (list (cons current last-unique) (add1 count))
            acc))
      (list '() 0)
      lst)))
  
  (count-unique nums))''',
  '''#lang racket

; Problem: Climbing Stairs
; Third solution using matrix exponentiation

(define (solve n)
  ; Matrix multiplication for fibonacci-like sequence
  (define (matrix-multiply A B)
    (vector 
     (+ (* (vector-ref A 0) (vector-ref B 0))
        (* (vector-ref A 1) (vector-ref B 2)))
     (+ (* (vector-ref A 0) (vector-ref B 1))
        (* (vector-ref A 1) (vector-ref B 3)))
     (+ (* (vector-ref A 2) (vector-ref B 0))
        (* (vector-ref A 3) (vector-ref B 2)))
     (+ (* (vector-ref A 2) (vector-ref B 1))
        (* (vector-ref A 3) (vector-ref B 3)))))
  
  ; Matrix power function
  (define (matrix-power M k)
    (cond
      [(= k 0) (vector 1 0 0 1)]  ; Identity matrix
      [(= k 1) M]
      [else
       (let* ([half (quotient k 2)]
              [half-power (matrix-power M half)])
         (if (even? k)
             (matrix-multiply half-power half-power)
             (matrix-multiply 
              (matrix-multiply half-power half-power) 
              M)))]))
  
  ; Base cases
  (cond 
    [(<= n 0) 0]
    [(= n 1) 1]
    [(= n 2) 2]
    
    ; Use matrix exponentiation for climbing ways
    [else
     (vector-ref 
      (matrix-power 
       (vector 1 1 1 0)  ; Transformation matrix
       (- n 2)) 
      0)]))''',
      '''#lang racket

; Problem: Maximum Subarray
; Third solution using divide and conquer approach

(define (solve nums)
  ; Divide and conquer max subarray sum
  (define (max-crossing-sum arr low mid high)
    (define left-sum 
      (let loop ([i mid]
                 [sum 0]
                 [max-sum (- (expt 2 31))])
        (if (< i low)
            max-sum
            (let* ([new-sum (+ sum (list-ref arr i))]
                   [new-max (max max-sum new-sum)])
              (loop (sub1 i) new-sum new-max)))))
    
    (define right-sum
      (let loop ([i (add1 mid)]
                 [sum 0]
                 [max-sum (- (expt 2 31))])
        (if (> i high)
            max-sum
            (let* ([new-sum (+ sum (list-ref arr i))]
                   [new-max (max max-sum new-sum)])
              (loop (add1 i) new-sum new-max)))))
    
    (+ left-sum right-sum))
  
  ; Recursive max subarray function
  (define (max-subarray-sum arr low high)
    ; Base case: single element
    (if (= low high)
        (list-ref arr low)
        
        ; Divide
        (let* ([mid (quotient (+ low high) 2)]
               [left-sum (max-subarray-sum arr low mid)]
               [right-sum (max-subarray-sum arr (add1 mid) high)]
               [cross-sum (max-crossing-sum arr low mid high)])
          
          ; Conquer: find maximum of three possibilities
          (max left-sum right-sum cross-sum))))
  
  ; Invoke divide and conquer
  (max-subarray-sum nums 0 (sub1 (length nums))))'''
    ]],
    "gemini":[[
'''#lang racket

(define (solve nums target)
  (let loop ([nums nums] [seen (make-hash)])
    (cond
      [(null? nums) #f]
      [(hash-has-key? seen (- target (car nums)))
       (let ([complement (- target (car nums))])
         (list (hash-ref seen complement) 0))]
       )
      [else (hash-set! seen (car nums) (length nums) - 1)
            (loop (cdr nums) seen)])))''',
'''#lang racket
(define (solve x)
  (let loop ([x x] [rev 0])
    (cond
      [(zero? x) rev]
      [(< (abs rev) (expt 2 31))
       (loop (quotient x 10) (+ (* rev 10) (modulo x 10)))]
      [else 0])))''',
'''#lang racket
(define (solve x)
  (let loop ([x x] [rev 0])
    (cond
      [(zero? x) (= x rev)]
      [(< (abs rev) (expt 2 31))
       (loop (quotient x 10) (+ (* rev 10) (modulo x 10)))]
      [else #f])))''',
'''#lang racket
(define (solve n)
  (for/list ([i (in-range 1 (add1 n))])
    (cond
      [(zero? (modulo i 15)) "FizzBuzz"]
      [(zero? (modulo i 3)) "Fizz"]
      [(zero? (modulo i 5)) "Buzz"]
      [else (number->string i)])))''',
'''#lang racket
(define (solve s)
  (let loop ([s s] [stack '()])
    (cond
      [(null? s) (null? stack)]
      [(memq (car s) '(#\( #\{ #\[))
       (loop (cdr s) (cons (car s) stack))]
      [(memq (car s) '(#\) #\} #\]))
       (cond
         [(null? stack) #f]
         [(memq (car stack) `(, (car s)))
          (loop (cdr s) (cdr stack))]
         [else #f])]
      [else #f])))''',
'''#lang racket
(define (solve nums)
  (let loop ([nums nums] [i 1])
    (cond
      [(null? (cdr nums)) (length nums)]
      [(= (car nums) (cadr nums))
       (loop (cdr nums) i)]
      [else (set-car! (vector-ref nums i) (cadr nums))
            (loop (cdr nums) (add1 i)))])))''',
'''#lang racket
(define (solve n)
  (let loop ([n n] [a 1] [b 1])
    (cond
      [(zero? n) a]
      [else (loop (- n 1) b (+ a b))])))''',
'''#lang racket
(define (solve nums)
  (let loop ([nums nums] [max-so-far 0] [max-ending-here 0])
    (cond
      [(null? nums) max-so-far]
      [else (set! max-ending-here (max 0 (+ max-ending-here (car nums))))
            (set! max-so-far (max max-so-far max-ending-here))
            (loop (cdr nums) max-so-far max-ending-here)])))'''
    ],
              ["""
#lang racket

(define (solve nums target)
  (let ([seen (make-hash)])
    (for ([i (in-range (length nums))])
      (let ([complement (- target (vector-ref nums i))])
        (when (hash-has-key? seen complement)
          (return (list (hash-ref seen complement) i))))))
    (hash-set! seen (vector-ref nums i) i)
    #f))
""",
"""
#lang racket

(define (solve x)
  (let loop ([x x] [sign (if (< x 0) -1 1)] [rev 0])
    (cond
      [(zero? x) (* sign rev)]
      [(< (abs rev) (expt 2 31))
       (loop (quotient x 10) sign (+ (* rev 10) (modulo x 10)))]
      [else 0])))
""",
"""
#lang racket

(define (solve x)
  (let loop ([x x] [rev 0])
    (cond
      [(zero? x) (= x rev)]
      [(< (abs rev) (expt 2 31))
       (loop (quotient x 10) (+ (* rev 10) (modulo x 10)))]
      [else #f])))
""",
"""
#lang racket

(define (solve n)
  (for/list ([i (in-range 1 (add1 n))])
    (cond
      [(zero? (modulo i 15)) "FizzBuzz"]
      [else (cond
                [(zero? (modulo i 3)) "Fizz"]
                [(zero? (modulo i 5)) "Buzz"]
                [else (number->string i)])])))
""",
"""
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
""",
"""
#lang racket

(define (solve nums)
  (let ([n (length nums)])
    (let loop ([i 0] [j 1])
      (cond
        [(>= j n) i]
        [(= (vector-ref nums i) (vector-ref nums j))
         (loop i (add1 j))]
        [else (vector-set! nums (add1 i) (vector-ref nums j))
               (loop (add1 i) (add1 j))])))
    n))
""",
"""
#lang racket

(define (solve n)
  (let loop ([n n] [prev 1] [curr 1])
    (cond
      [(zero? n) prev]
      [else (loop (- n 1) curr (+ prev curr))])))
""",
"""
#lang racket

(define (solve nums)
  (let loop ([nums nums] [max-so-far (car nums)])
    (cond
      [(null? nums) max-so-far]
      [(let ([curr (max (car nums) (+ max-so-far (car nums)))])
           (loop (cdr nums) (max max-so-far curr))))])))
"""], ["""
#lang racket

(define (solve nums target)
  (for/list ([i (in-range (length nums))])
    (let ([complement (- target (vector-ref nums i))])
      (for/list ([j (in-range (add1 i) (length nums))])
        (when (= complement (vector-ref nums j))
          (return (list i j)))))))
  #f)
""",
"""
#lang racket

(define (solve x)
  (let ([sign (if (< x 0) -1 1)]
        [x (abs x)])
    (let loop ([x x] [rev 0])
      (cond
        [(zero? x) (* sign rev)]
        [(< (abs rev) (expt 2 31))
         (loop (quotient x 10) (+ (* rev 10) (modulo x 10)))]
        [else 0]))))
""",
"""
#lang racket

(define (solve x)
  (string=? (string x) (string-reverse (string x))))
""",
"""
#lang racket

(define (solve n)
  (for/list ([i (in-range 1 (add1 n))])
    (cond
      [(zero? (modulo i 15)) "FizzBuzz"]
      [(zero? (modulo i 3)) "Fizz"]
      [(zero? (modulo i 5)) "Buzz"]
      [else (number->string i)])))
""",
"""
#lang racket

(define (solve s)
  (let loop ([s s] [stack '()])
    (cond
      [(null? s) (null? stack)]
      [(memq (car s) '(#\( #\{ #\[))
       (loop (cdr s) (cons (car s) stack))]
      [(memq (car s) '(#\) #\} #\]))
       (cond
         [(null? stack) #f]
         [(memq (car stack) `(, (car s)))
          (loop (cdr s) (cdr stack))]
         [else #f])]
      [else #f])))
""",
"""
#lang racket

(define (solve nums)
  (let loop ([nums nums] [i 0])
    (cond
      [(null? nums) i]
      [(= (car nums) (cadr nums))
       (loop (cdr nums) i)]
      [else (loop (cdr nums) (add1 i))])))
""",
"""
#lang racket

(define (solve n)
  (let loop ([n n] [fibs (list 0 1)])
    (cond
      [(zero? n) (car fibs)]
      [else (loop (- n 1) (cdr fibs))]))))
""",
"""
#lang racket

(define (solve nums)
  (let loop ([nums nums] [max-so-far (car nums)] [curr-sum (car nums)])
    (cond
      [(null? nums) max-so-far]
      [(let ([new-sum (max (car nums) (+ curr-sum (car nums)))])
           (loop (cdr nums) (max max-so-far new-sum) new-sum)))])))
"""]]
}