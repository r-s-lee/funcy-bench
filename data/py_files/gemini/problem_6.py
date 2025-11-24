def solve(n):
    if n == 1 or n == 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
print(solve(2) == 2)
print(solve(3) == 3)
print(solve(5) == 8)
print(solve(10) == 89)
print(solve(20) == 10946)
