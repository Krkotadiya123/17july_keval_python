"""Q.9 Write a Python function that takes two lists and returns true if they have
at least one common member."""

def abc(a,list2):
    for i in a:
        if i in list2:
            return i,list2
        
a=[1,2,3,4,5]
list2=[5,6,7,8,9]

bcd=abc(a,list2)

if bcd:
     print("this is one common number.")
else:
    print("this is do not multy common number.")



    





 

