def solve(nums):
    """
    Finds the contiguous subarray with the largest sum.
    
    Args:
        nums (List[int]): The input array.
    
    Returns:
        int: The largest sum.
    """
    max_current = max_global = nums[0]
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        max_global = max(max_global, max_current)
    return max_global
    
print(solve([-2,1,-3,4,-1,2,1,-5,4]) == 6)
print(solve([1]) == 1)
print(solve([5,4,-1,7,8]) == 23)
print(solve([-1,-2,-3]) == -1)
print(solve([10,-1,-1,10]) == 18)
