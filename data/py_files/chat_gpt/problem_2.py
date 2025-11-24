def solve(x):
    """
    Checks if an integer is a palindrome.
    
    Args:
        x (int): The integer to check.
    
    Returns:
        bool: True if x is a palindrome, False otherwise.
    """
    if x < 0:
        return False
    str_x = str(x)
    return str_x == str_x[::-1]
    
print(solve(121) == True)
print(solve(-121) == False)
print(solve(10) == False)
print(solve(0) == True)
print(solve(1234321) == True)
