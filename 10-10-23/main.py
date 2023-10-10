'''
take a string an perform the fpollowing string handeling function:
1 find the lenghth of string
2 convert the given string to lower case
3 convert the given string to uppercase
4 perform the slicing method to th egivcen string 
5 find the index of any character from the given string 
6 find the number count of any character in the given string 
'''

input_str = "Hello My Name Is Ayush"
find_char = 'a'

length = len(input_str)
print("1. Length of string is: ",length)

lower = input_str.lower()
print("2. String in Lowercase: ",lower)

upper = input_str.upper()
print("3. String in Uppercase: ",upper)

slicied_string = input_str[3:6]
print("4. Sliced string is: ", slicied_string)

find_index = input_str.find(find_char)
print(f"5. Index of '{find_char}' in the sting is: ", find_index)

count_char = input_str.count(find_char)
print(f"6. Count of '{find_char}' in the string is: ", count_char)