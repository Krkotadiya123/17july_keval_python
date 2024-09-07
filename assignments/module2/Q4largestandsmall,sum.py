"""Q.4->Write a Python function to get the largest number, smallest num and sum
of all from a list."""
def largest (number):


    print("largest",max(number))
    print("smallest",min(number))
    print("sum",sum(number))


total_numbers=int(input("enter total number :"))

number=[]

for i in range(total_numbers):
    nm=int(input("enter number:"))
    number.append(nm)

largest(number)





