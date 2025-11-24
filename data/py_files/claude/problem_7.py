def solve(nums):
    """
    Find contiguous subarray with largest sum.
    
    Time complexity: O(n)
    Space complexity: O(1)
    """
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        # Decide whether to start a new subarray or extend existing
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum
print(solve([-2,1,-3,4,-1,2,1,-5,4]) == 6)
print(solve([1]) == 1)
print(solve([5,4,-1,7,8]) == 23)
print(solve([-1,-2,-3]) == -1)
print(solve([10,-1,-1,10]) == 18)
