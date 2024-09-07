"""Q48. Write a Python function to calculate the factorial of a number (anonnegative integer) """

def Factorial(n):
    count = 1

    if n<0:
        print("Number is Negative........ Please Enter Positive Number")
    elif n == 0:
        print("Number Is ZERO....")

    elif n >=0:


        for i in range(1,n+1):
            count *=i

        print("Number is= ",n,"Factorial Is= ",count)

a=int(input("Enter a Number For Find FActorial: "))

Factorial(a)