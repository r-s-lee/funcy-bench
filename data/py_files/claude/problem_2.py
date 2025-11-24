def solve(x):
    """
    Determine if an integer is a palindrome.
    
    Time complexity: O(log x)
    Space complexity: O(1)
    """
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    # Reverse half of the number
    original = x
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    
    # Check palindrome condition
    return x == reversed_half or x == reversed_half // 10
print(solve(121) == True)
print(solve(-121) == False)
print(solve(10) == False)
print(solve(0) == True)
print(solve(1234321) == True)
