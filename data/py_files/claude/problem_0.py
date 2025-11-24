def solve(nums, target):
    """
    Find indices of two numbers that add up to target.
    
    Time complexity: O(n)
    Space complexity: O(n)
    """
    # Map to store complement values
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []  # No solution found
    
print(solve([2,7,11,15],9) == [0, 1])
print(solve([3,2,4],6) == [1, 2])
print(solve([3,3],6) == [0, 1])
print(solve([1,5,5,3],10) == [1, 2])
print(solve([0,0,4,-2,2],2) == [2, 3])
