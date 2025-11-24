def solve(x):
    if x < 0:
        return False
    rev = 0
    original = x
    while x > 0:
        rev = rev * 10 + x % 10
        x //= 10
    return rev == original
print(solve(121) == True)
print(solve(-121) == False)
print(solve(10) == False)
print(solve(0) == True)
print(solve(1234321) == True)
