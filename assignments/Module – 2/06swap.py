"""Write python program that swap two number with temp variable and
without temp variable."""

"""x=10 #without temp variable
y=5

x,y=y,x

print(f"x={x} and y={y} swap{x,y}")"""
x = 10
y = 5
# with temp variable

temp = x
x = y
y = temp

print(f"x={x} and y={y} swap temp")

