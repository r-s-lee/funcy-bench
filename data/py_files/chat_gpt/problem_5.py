def solve(nums):
    """
    Removes duplicates from a sorted array in-place.
    
    Args:
        nums (List[int]): The sorted array.
    
    Returns:
        int: The new length of the array.
    """
    if not nums:
        return 0
    write_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[write_index] = nums[i]
            write_index += 1
    return write_index
    
print(solve([1,1,2]) == 2)
print(solve([0,0,1,1,1,2,2,3,3,4]) == 5)
print(solve([1,1,1,1]) == 1)
print(solve([1,2,3]) == 3)
print(solve([1]) == 1)
