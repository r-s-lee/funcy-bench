def solve(x):
    """
    Reverses the digits of a 32-bit signed integer.
    
    Args:
        x (int): The integer to reverse.
    
    Returns:
        int: The reversed integer or 0 if out of bounds.
    """
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_x = int(str(x)[::-1]) * sign
    if -2**31 <= reversed_x <= 2**31 - 1:
        return reversed_x
    return 0
    
print(solve(123) == 321)
print(solve(-123) == -321)
print(solve(120) == 21)
print(solve(1534236469) == 0)
print(solve(-2147483648) == 0)
