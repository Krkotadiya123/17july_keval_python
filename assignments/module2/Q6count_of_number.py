"""Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings"""


def count_string(number):
    count = 0
    for s in number:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count 

use = int(input("Enter total strings:"))

number_list = []

for i in range(use):
    string = input("Enter string: ")
    number_list.append(string)

count=count_string(number_list)
print("Count of valid strings:", count)









"""def count_special_strings(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count

# Get user input as a list of strings, separated by spaces
user_input = input("Enter a list of strings separated by spaces: ")

# Split the input into a list of strings
strings_list = user_input.split()

# Call the function and print the result
result = count_special_strings(strings_list)
print("Number of strings where the first and last character are the same and length is 2 or more:", result)"""

