''' Q44. Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary. 
Sample data: {'1': ['a','b'], '2': ['c','d']} '''

A={1:['a','b'], 2:['c','d']}

B=[]
print(A)

for i in A.values():
    B.append(i)

l=len(B)

for j in range(l):
    for k in range(l):
        X=B[0][j]+B[1][k]
        print(X,end=" ")