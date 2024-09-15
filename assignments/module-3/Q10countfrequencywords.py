# Write a Python program to count the frequency of words in a file.

fl=open('kev.txt')
data=fl.read()

count=0
ch=input("count the frequency of words: ")

for i in data:
    if i==ch:
        count+=len(i)

print(count)