"""Q51.Write a Python function that checks whether a passed string is palindrome or not"""

def palindrome_str(a):
    if a == a[::-1]:
        print(f"The string '{a}' is a palindrome.")
    else:
        print(f"The string '{a}' is not a palindrome.")

s = input("Enter a string: ")
palindrome_str(s)
