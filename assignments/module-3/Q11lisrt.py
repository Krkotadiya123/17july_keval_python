# Write a Python program to write a list to a file. 


list=['Rajkot','Diu','Goa','Jamanagar','Bhavnagar','Dwarka','Somanath']


fl=open('kev.txt','w')

for i in list:
    fl.write(f"{i}\n")