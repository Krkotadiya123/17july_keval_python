"""Write a Python program to count the occurrences of each word in a
given sentence"""
str1={}
str="this is  python."
count=str.lower().split()

for str in count:
    if str in str1:
        str1[str]+=1
    else:
        str1[str]=1
print(count)

