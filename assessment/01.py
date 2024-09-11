import datetime


def gen_not():

            print("For generating note:")
            file_name = input("enter file name:").strip()
            content = input("enter content: ")
            c_datetime = datetime.datetime.now()
            file=open('note.txt','a')
            file.write('---------------------------\n')
            file.write(f'{c_datetime}\n')
            file.write(f'Title: {file_name}\n')
            file.write(f'content: {content}\n')
            file.close()
            
            print("Note created successfully")
   

def view_not():
    read_file=open('note.txt','r')
    print(read_file.read())

# def for_exit():
    # print("for exit")



print("welcome to E-note book\n")


while True:
    print("1.for generate note:")
    print("2.for  view note:")
    print("3.for exit")
    choice=int(input("enter choice 1-3:"))

    if choice==1:
        gen_not()
    elif choice==2:
        view_not()
    elif choice ==3:
        break
    
    # else:
        # print("not  number:")
            
# print("welcome to python e-note book ")
   






