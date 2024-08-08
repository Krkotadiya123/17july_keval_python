"""Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string."""

name=input("enter string:")
substring=name.split()
print("substring:",substring)
if len(substring)>5:
    print("string is poor")
else:
    print("string is not poor")

