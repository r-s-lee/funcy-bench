def solve(nums, target):
    """
    Finds two indices of numbers in the list that add up to the target.
    
    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.
    
    Returns:
        List[int]: Indices of the two numbers.
    """
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    
print(solve([2,7,11,15],9) == [0, 1])
print(solve([3,2,4],6) == [1, 2])
print(solve([3,3],6) == [0, 1])
print(solve([1,5,5,3],10) == [1, 2])
print(solve([0,0,4,-2,2],2) == [2, 3])
