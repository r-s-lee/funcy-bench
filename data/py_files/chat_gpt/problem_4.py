def solve(s):
    """
    Checks if a string has valid parentheses.
    
    Args:
        s (str): The string to check.
    
    Returns:
        bool: True if the string is valid, False otherwise.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
    
print(solve("()") == True)
print(solve("()[]{}") == True)
print(solve("(]") == False)
print(solve("([)]") == False)
print(solve("{") == False)
