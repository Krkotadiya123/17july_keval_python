"""Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero."""
a=input("enter number")
b=input("enter number")
c=input("enter number")
if a==b or a==c or b==c:
    print(0)
else:
    print(a + b + c)
