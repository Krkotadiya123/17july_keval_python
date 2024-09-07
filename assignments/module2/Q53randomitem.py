"""Q53. How can you pick a random item from a list or tuple?"""


import random

a=["Rajkot","Diu","Gonal","Bhavngar","Kachh"]

b=(5,6,5,20,54,30,65,70,20)

list=random.choice(a)
Tuple=random.choice(b)

print(list)
print("Random Word Choice in= ",a,'\n')


print(Tuple)
print("Random Number Select in= ",b)