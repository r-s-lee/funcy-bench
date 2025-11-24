def solve(nums):
    """
    Remove duplicates in-place and return new length.
    
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if not nums:
        return 0
    
    # Two-pointer technique
    write_pointer = 1
    
    for read_pointer in range(1, len(nums)):
        if nums[read_pointer] != nums[read_pointer - 1]:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1
    
    return write_pointer
print(solve([1,1,2]) == 2)
print(solve([0,0,1,1,1,2,2,3,3,4]) == 5)
print(solve([1,1,1,1]) == 1)
print(solve([1,2,3]) == 3)
print(solve([1]) == 1)
