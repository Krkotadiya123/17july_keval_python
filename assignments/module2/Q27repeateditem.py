""" Q27. Write a Python program to find the repeated items of a tuple."""

a=(1,2,3,4,5,6,7,8,9,0,1)

b=[]

for i in a:
    if a.count(i) >=2:
        b.append(i)

print(a)
print(tuple(set(b)))