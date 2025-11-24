def solve(nums):
    max_so_far = max_ending_here = nums[0]
    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
print(solve([-2,1,-3,4,-1,2,1,-5,4]) == 6)
print(solve([1]) == 1)
print(solve([5,4,-1,7,8]) == 23)
print(solve([-1,-2,-3]) == -1)
print(solve([10,-1,-1,10]) == 18)
