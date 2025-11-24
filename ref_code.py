reference_code = {
    "chat_gpt": 
        [
    """def solve(nums, target):
    \"\"\"
    Finds two indices of numbers in the list that add up to the target.
    
    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.
    
    Returns:
        List[int]: Indices of the two numbers.
    \"\"\"
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    """,

    """def solve(x):
    \"\"\"
    Reverses the digits of a 32-bit signed integer.
    
    Args:
        x (int): The integer to reverse.
    
    Returns:
        int: The reversed integer or 0 if out of bounds.
    \"\"\"
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_x = int(str(x)[::-1]) * sign
    if -2**31 <= reversed_x <= 2**31 - 1:
        return reversed_x
    return 0
    """,

    """def solve(x):
    \"\"\"
    Checks if an integer is a palindrome.
    
    Args:
        x (int): The integer to check.
    
    Returns:
        bool: True if x is a palindrome, False otherwise.
    \"\"\"
    if x < 0:
        return False
    str_x = str(x)
    return str_x == str_x[::-1]
    """,

    """def solve(n):
    \"\"\"
    Generates the FizzBuzz sequence up to n.
    
    Args:
        n (int): The upper limit.
    
    Returns:
        List[str]: The FizzBuzz sequence.
    \"\"\"
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
    """,

    """def solve(s):
    \"\"\"
    Checks if a string has valid parentheses.
    
    Args:
        s (str): The string to check.
    
    Returns:
        bool: True if the string is valid, False otherwise.
    \"\"\"
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
    """,

    """def solve(nums):
    \"\"\"
    Removes duplicates from a sorted array in-place.
    
    Args:
        nums (List[int]): The sorted array.
    
    Returns:
        int: The new length of the array.
    \"\"\"
    if not nums:
        return 0
    write_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[write_index] = nums[i]
            write_index += 1
    return write_index
    """,

    """def solve(n):
    \"\"\"
    Calculates the number of distinct ways to climb to the top.
    
    Args:
        n (int): The number of steps to climb.
    
    Returns:
        int: The number of ways to climb.
    \"\"\"
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
    """,

    """def solve(nums):
    \"\"\"
    Finds the contiguous subarray with the largest sum.
    
    Args:
        nums (List[int]): The input array.
    
    Returns:
        int: The largest sum.
    \"\"\"
    max_current = max_global = nums[0]
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        max_global = max(max_global, max_current)
    return max_global
    """,
        ],
    "claude": 
        [
    '''def solve(nums, target):
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
    ''',

'''def solve(x):
    """
    Reverse the digits of an integer with 32-bit integer overflow check.
    
    Time complexity: O(log x)
    Space complexity: O(1)
    """
    # Handle sign
    sign = 1 if x >= 0 else -1
    x = abs(x)
    
    # Reverse digits
    reversed_num = 0
    while x:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    
    # Check 32-bit integer overflow
    reversed_num *= sign
    return reversed_num if -2**31 <= reversed_num <= 2**31 - 1 else 0''',

'''def solve(x):
    """
    Determine if an integer is a palindrome.
    
    Time complexity: O(log x)
    Space complexity: O(1)
    """
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    # Reverse half of the number
    original = x
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    
    # Check palindrome condition
    return x == reversed_half or x == reversed_half // 10''',

'''def solve(n):
    """
    Generate FizzBuzz sequence.
    
    Time complexity: O(n)
    Space complexity: O(n)
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result''',

'''def solve(s):
    """
    Check if parentheses are balanced and correctly nested.
    
    Time complexity: O(n)
    Space complexity: O(n)
    """
    # Map of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    # Stack to track opening brackets
    stack = []
    
    for char in s:
        if char in bracket_map:
            # If current is a closing bracket
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            # If current is an opening bracket
            stack.append(char)
    
    # Stack should be empty for valid parentheses
    return len(stack) == 0''',

'''def solve(nums):
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
    
    return write_pointer''',

'''def solve(n):
    """
    Count number of distinct ways to climb stairs.
    
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if n <= 2:
        return n
    
    # Dynamic programming with constant space
    prev1, prev2 = 2, 1
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1''',

'''def solve(nums):
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
    
    return max_sum''',
    ], "gemini":[
    """def solve(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []""",

        """def solve(x):
    rev = 0
    while x != 0:
        digit = x % 10
        x //= 10
        if rev > 2**31 // 10 or (rev == 2**31 // 10 and digit > 7):
            return 0
        if rev < -2**31 // 10 or (rev == -2**31 // 10 and digit < -8):
            return 0
        rev = rev * 10 + digit
    return rev""",

        """def solve(x):
    if x < 0:
        return False
    rev = 0
    original = x
    while x > 0:
        rev = rev * 10 + x % 10
        x //= 10
    return rev == original""",

        """def solve(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result""",

        """def solve(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack""",

        """def solve(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1""",

        """def solve(n):
    if n == 1 or n == 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]""",

        """def solve(nums):
    max_so_far = max_ending_here = nums[0]
    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far"""
    ]
}