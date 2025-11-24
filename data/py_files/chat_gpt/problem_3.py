def solve(n):
    """
    Generates the FizzBuzz sequence up to n.
    
    Args:
        n (int): The upper limit.
    
    Returns:
        List[str]: The FizzBuzz sequence.
    """
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
    
print(solve(15) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'])
print(solve(5) == ['1', '2', 'Fizz', '4', 'Buzz'])
print(solve(3) == ['1', '2', 'Fizz'])
print(solve(1) == ['1'])
print(solve(20) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz'])
