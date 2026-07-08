def view_student():
    file = open("student.txt","r")
    print(file.read())
    file.close()
    # with open("student.txt", "r") as file:
    #     print(file.read())


def add_student():
    name = input("Enter name:")
    marks = input("Enter marks:")

    with  open("student.txt","a") as file:
        file.write(f"{name} {marks}\n")

    print("Student added successfully.")
   

def search_student():
    name = input("Enter the name:")

    found = False

    with open("student.txt","r") as file:
        for line in file:
            if name in line:
                found = True
                print("Student Found")
                break

            if not found:
                print("Student Not found")

def delete_student():
    name = input("Enter the name :")
    
    records =[]
    found = False
    
    with open("Student.txt","r") as file:
        for line in file:
            if name not in line:
                records.append(line)
            else:
                found = True
    with open ("student.txt","w") as file:
        for line in records:
            file.write(line)
    
    if found:
        print("Student deleted successfully.")
    else:
        print("Student Not Found")
    
def menu():
    while True:
        print("\n===== Student Record Manager ====")
        print("1 .view student")
        print("2 .add student")
        print("3 .search student")
        print("4. delete student")
        print("5 . exit")

        choice = input("Enter Choice :")

        if choice == "1":
            view_student()

        elif choice == "2":
            add_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("exit")
            break

        else:
            print("Invalid input")
        
menu()
            


        
            

         
     