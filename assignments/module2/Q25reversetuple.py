# Q25. Write a Python program to reverse a tuple. 

a=[]

X=int(input("Enter a num of car:"))

for i in range(X):
    b=input("Enter a car Name:")
    a.append(b)

R=tuple(a)
c=R[::-1]

print(a)
print(c)