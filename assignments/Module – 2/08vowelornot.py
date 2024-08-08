"""Write a Python program to test whether a passed letter is a vowel or
not."""

a= input("Enter a letter: ")

if a in 'a,e,i,o,u,A,E,I,O,U':
    print(f" this is a vowel={a}")
else:
    print(f"this is not a vowel.{a}")
