import pymysql

# Database connection
def pyh():
    try:
        py_ph = pymysql.connect(host='localhost', user='root', password='', database='medicledb')
        cursor = py_ph.cursor()
        print("Database connected!")
        return py_ph,cursor  
    except Exception as e:
        print(e)

#Table Create
create_ad="create table admin(id integer primary key auto_increment,name text,password int,city text)"

tbm="create table manager(id integer primary key auto_increment,name text,password int)"

mc="create table mc(id integer primary key auto_increment,name text, quantity int,price int )"


py_ph,cursor=pyh()
if py_ph and cursor:
    try:
            cursor.execute(create_ad)
            cursor.execute(tbm)
            cursor.execute(mc)
            py_ph.commit()
            print("Tables created")
    except Exception as e:
            print(e)


class Admin:
    def __init__(self, py_ph, cursor):
        self.py_ph = py_ph
        self.cursor = cursor

    def register(self):
        try:
            name = input("Enter name: ")
            password = int(input("Enter password: "))
            city = input("Enter city: ")
            self.cursor.execute("INSERT INTO admin (name, password, city) VALUES (%s, %s, %s)", (name,password,city))
            self.py_ph.commit()
            print(" registered successfully!")
        except Exception as e:
            print(e)

    def login(self):
        try:
            name = input("enter name: ")
            password = int(input("enter password: "))
            self.cursor.execute("SELECT * FROM admin WHERE name=%s AND password=%s", (name, password))
            result = self.cursor.fetchone()
            if result:
                print(" login successful!")
            else:
                print("Login failed.")
        except Exception as e:
            print(e)

    def view_medicine(self):
        try:
            self.cursor.execute("SELECT * FROM medicine")
            medicines = self.cursor.fetchall()
            for med in medicines:
                print(f"ID: {medicines[0]}, name:{medicines[1]},quantity:{medicines[2]},Price:{medicines[3]}")
        except Exception as e:
            print(e)

# Pharmacy Manager class
class PharmacyManager:
    def __init__(self,py_ph, cursor):
        self.py_ph = py_ph
        self.cursor = cursor

    def register(self):
        try:
            name = input("Enter name: ")
            password = int(input("enter password: "))
            self.cursor.execute("INSERT INTO manager (name, password) VALUES (%s, %s)", (name, password))
            self.py_ph.commit()
            print("Pharmacy Manager registered")
        except Exception as e:
            print(e)

    def login(self):
        try:
            name = input("enter name: ")
            password = int(input("enter password: "))
            self.cursor.execute("SELECT * FROM manager WHERE name=%s AND password=%s", (name, password))
            result = self.cursor.fetchone()
            if result:
                print("Login successful!")
            else:
                print("failed.")
        except Exception as e:
            print(e)

    def add_medicine(self):
        try:
            name = input("enter medicine name: ")
            quantity = int(input("enter quantity: "))
            price = int(input("Enter price: "))
            self.cursor.execute("INSERT INTO medicine (name, quantity, price) VALUES (%s, %s, %s)", (name, quantity, price))
            self.py_ph.commit()
            print("Medicine added")
        except Exception as e:
            print(e)

    def view_medicine(self):
        try:
            self.cursor.execute("SELECT * FROM medicine")
            medicines = self.cursor.fetchall()
            for med in medicines:
                print(f"ID: {med[0]},name:{med[1]},quantity:{med[2]}, Price:{med[3]}")
        except Exception as e:
            print(e)

    def delete_medicine(self):
        try:
            med_id = int(input("enter medicine ID to delete: "))
            self.cursor.execute("dELETE FROM medicine WHERE id=%s", (med_id,))
            self.py_ph.commit()
            print(" deleted successfully!")
        except Exception as e:
            print(e)

# Main function to manage the program flow
def main():
    while True:
        print("\n1. admin")
        print("2. pharmacy manager")
      
        user_type = input("choose any one: ")

        if user_type == "1":
            admin = Admin(py_ph, cursor)
            while True:
                print("1. Register admin\n")
                print("2. admin login\n")
                print("3. view medicines\n")
                print("4. Exit\n")
                choice = input("Enter choice: ")
                if choice == "1":
                    admin.register()
                elif choice == "2":
                    admin.login()
                elif choice == "3":
                    admin.view_medicine()
                elif choice == "4":
                    break
                else:
                    print("invalid choice:")

        elif user_type == "2":
            pm = PharmacyManager(py_ph, cursor)
            while True:
                print("1. Register Pharmacy Manager\n")
                print("2. login Pharmacy Manager\n")
                print("3. add Medicine\n")
                print("4. view Medicines\n")
                print("5. delete Medicine\n")
                print("6. exit\n")
                choice = input("Enter choice: ")
                if choice == "1":
                    pm.register()
                elif choice == "2":
                    pm.login()
                elif choice == "3":
                    pm.add_medicine()
                elif choice == "4":
                    pm.view_medicine()
                elif choice == "5":
                    pm.delete_medicine()
                elif choice == "6":
                    break
                else:
                    print("invalid choice:")



main()