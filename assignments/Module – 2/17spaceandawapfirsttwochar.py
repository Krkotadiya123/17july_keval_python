"""Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string."""
a=input("enter string1:")
b=input("enter string2:")

newstring=a + " " + b

print(newstring)

a,b=b,a #swap
newstring=a + " "+ b

print(newstring)

