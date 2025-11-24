def solve(s):
    """
    Check if parentheses are balanced and correctly nested.
    
    Time complexity: O(n)
    Space complexity: O(n)
    """
    # Map of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    # Stack to track opening brackets
    stack = []
    
    for char in s:
        if char in bracket_map:
            # If current is a closing bracket
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            # If current is an opening bracket
            stack.append(char)
    
    # Stack should be empty for valid parentheses
    return len(stack) == 0
print(solve("()") == True)
print(solve("()[]{}") == True)
print(solve("(]") == False)
print(solve("([)]") == False)
print(solve("{") == False)
