s
print(solve("()") == True)
print(solve("()[]{}") == True)
print(solve("(]") == False)
print(solve("([)]") == False)
print(solve("{") == False)
