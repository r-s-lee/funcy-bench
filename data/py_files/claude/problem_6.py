def solve(n):
    """
    Count number of distinct ways to climb stairs.
    
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if n <= 2:
        return n
    
    # Dynamic programming with constant space
    prev1, prev2 = 2, 1
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1
print(solve(2) == 2)
print(solve(3) == 3)
print(solve(5) == 8)
print(solve(10) == 89)
print(solve(20) == 10946)
