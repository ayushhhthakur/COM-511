# Given string
input_string = "Welcome to Python World"

# 1. Count the number of alphabets in the given string
alphabet_count = sum(1 for char in input_string if char.isalpha())

print(f"Number of alphabets in the string: {alphabet_count}")

# 2. Extract characters from a given range in the string
start_index = 8  # Start index (inclusive)
end_index = 14   # End index (exclusive)

if 0 <= start_index < end_index <= len(input_string):
    extracted_characters = input_string[start_index:end_index]
    print(f"Extracted characters from index {start_index} to {end_index - 1}: '{extracted_characters}'")
else:
    print("Invalid range. Ensure that 0 <= start_index < end_index <= len(input_string).")

# 3. Check if the string is alphanumeric
is_alphanumeric = input_string.isalnum()
if is_alphanumeric:
    print("The string is alphanumeric.")
else:
    print("The string is not alphanumeric.")
