# Write a Python program to copy the contents of a file to another file. 
f1=open('kev.txt','a')
f2=open('kev1.txt','r')

for contents in f2:
    f1.write(contents)