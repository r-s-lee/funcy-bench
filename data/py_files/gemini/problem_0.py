def solve(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
print(solve([2,7,11,15],9) == [0, 1])
print(solve([3,2,4],6) == [1, 2])
print(solve([3,3],6) == [0, 1])
print(solve([1,5,5,3],10) == [1, 2])
print(solve([0,0,4,-2,2],2) == [2, 3])
