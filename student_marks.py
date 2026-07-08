students = {
   "Ram"  : 85,
    "Karan" : 95,
    "Priya" : 98

}

def view_students():
     for name, marks in students.items():
        print(f"{name} : {marks}")
   

def add_students():
    name = input("Enter student name:")
    mark = int(input("Enter the student marks"))

    if name  in students:
        print("f{name} already in document.")
    else:
        students[name] = mark
        print(f"{name} : {mark} added successfully.")

def search_student():
        name = input("Enter name of the student:")

        if name in  students:
             print(f"{name}'s  marks are {students[name]}:")
        else:
             print("Student not found")
        
def delete_students():
    name = input("Enter the student name:")

    if name in students:
        del students[name]
        print(f"{name} deleted succesfully.")

    else:
        print(f"{name} is not found")

def update_student():
     name = input("Enter student name:")

     if name in students:
          new_marks = int(input("Enter new marks:"))
          students[name] = new_marks
          print("Marks updated successfully.")

     else:
          print("Student not found.")



def menu():
     while True:
          print("1. view students")
          print("2. add  students")
          print("3. search students")
          print("4. delete students")
          print("5. exit")

          choice = input("enter choice :")

          if choice == "1":
               view_students()
          elif choice == "2":
               add_students()
          elif choice == "3":
               search_student()
          elif choice == "4":
               delete_students()
          elif choice == "5":
               print("exit")
               break
          
          else:
               print("Invalid choice")

menu()
               
      
    
        


    
        



