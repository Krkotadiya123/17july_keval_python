"""Q.12 Write a Python program to convert a list of characters into a string."""

def convert(string1):
    string=""
    for i in string1:
        string+=i
        return string

a=input("enter total string:")
string1=[]
for k in range(a):

    b=input("enter string:")
    string1.append(k)

s=convert(string1)
print("convert string:",s)


    
