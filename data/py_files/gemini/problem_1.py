def solve(x):
    rev = 0
    while x != 0:
        digit = x % 10
        x //= 10
        if rev > 2**31 // 10 or (rev == 2**31 // 10 and digit > 7):
            return 0
        if rev < -2**31 // 10 or (rev == -2**31 // 10 and digit < -8):
            return 0
        rev = rev * 10 + digit
    return rev
print(solve(123) == 321)
print(solve(-123) == -321)
print(solve(120) == 21)
print(solve(1534236469) == 0)
print(solve(-2147483648) == 0)
