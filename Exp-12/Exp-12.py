def max_of_three(a, b, c):
    return max(a, b, c)

def is_armstrong(number):
    num_str = str(number)
    order = len(num_str)
    sum_of_cubes = sum(int(digit) ** order for digit in num_str)
    return sum_of_cubes == number

# Example usage:
num1, num2, num3 = 5, 8, 3

# Finding the maximum of three numbers
max_value = max_of_three(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, and {num3} is: {max_value}")

# Checking if a number is an Armstrong number
num_to_check = 153
result = is_armstrong(num_to_check)
print(f"Is {num_to_check} an Armstrong number? {result}")
