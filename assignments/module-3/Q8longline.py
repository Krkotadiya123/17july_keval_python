# Write a python program to find the longest words.


fl=open('kev.txt')
file=fl.readlines()

max=max(file,key=len)
print(max)