def solve(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
print(solve([1,1,2]) == 2)
print(solve([0,0,1,1,1,2,2,3,3,4]) == 5)
print(solve([1,1,1,1]) == 1)
print(solve([1,2,3]) == 3)
print(solve([1]) == 1)
