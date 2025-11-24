def solve(x):
    """
    Reverse the digits of an integer with 32-bit integer overflow check.
    
    Time complexity: O(log x)
    Space complexity: O(1)
    """
    # Handle sign
    sign = 1 if x >= 0 else -1
    x = abs(x)
    
    # Reverse digits
    reversed_num = 0
    while x:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    
    # Check 32-bit integer overflow
    reversed_num *= sign
    return reversed_num if -2**31 <= reversed_num <= 2**31 - 1 else 0
print(solve(123) == 321)
print(solve(-123) == -321)
print(solve(120) == 21)
print(solve(1534236469) == 0)
print(solve(-2147483648) == 0)
