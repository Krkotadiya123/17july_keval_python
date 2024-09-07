"""Q.10Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30."""

def square():
    square=[]
    for i in range(1, 31):
    
        square.append(i**2)
        print(i)
    return square
    

squares = square()

print("First 5 elements:", squares[:5])
print("Last 5 elements:", squares[-5:])

