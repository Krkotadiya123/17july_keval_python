'''Write a Python program to get the Fibonacci series of given range.'''
x = 0
y = 1
fact=0

num = int(input("enter number: "))

if num<0:
    print()
for i in range(num):
    print(x, end=" ")
    z = x + y
    x = y
    y = z


print("fibonacc series of range:", num,fact)