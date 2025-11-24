def solve(n):
    """
    Calculates the number of distinct ways to climb to the top.
    
    Args:
        n (int): The number of steps to climb.
    
    Returns:
        int: The number of ways to climb.
    """
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
    
print(solve(2) == 2)
print(solve(3) == 3)
print(solve(5) == 8)
print(solve(10) == 89)
print(solve(20) == 10946)
