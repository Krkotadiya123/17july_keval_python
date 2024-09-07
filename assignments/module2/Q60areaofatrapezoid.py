"""Q60. Write a Python program to calculate the 5 """

def trapezoid(Top,Bottom,Height):
    trapezoid=((Top+Bottom)/2)*Height
    print(trapezoid)

t=int(input("Enter Value of Top: "))
b=int(input("Enter Value of Bottom: "))
h=int(input("Enter Value of Hight: "))

trapezoid(t,b,h)