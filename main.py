from src.funciones import request_name,request_course,request_int,add_student,student_list,search_student,update_student,remove_student
from src.archivos import save_csv

list_students = [
        {"id": 1042425120,
        "name": "Isaac",
        "age": 20,
        "course": "python",
        "status": "Active",}
        ]

print("Student Management System")

action = 0
while action != 7:

    print("-Menu-----------------------------".upper())
    print("| 1 → Register new students      |")
    print("| 2 → View student list          |")
    print("| 3 → Search for student         |")
    print("| 4 → Update student information |")
    print("| 5 → Remove students            |")
    print("| 6 → Save CSV                   |")
    print("| 7 → Exit                       |")
    print("-" * 34)

    try:
        action = int(input("Select the action to perform: "))
        print()
    except ValueError:
        print()
        print("Error: Only numbers are allowed\n")
        continue
        
    # Add student to list
    if action == 1:
        print("----Register new students----\n".upper())
        
        follow = "yes"

        while follow in ("y", "yes"):

            id = request_int("Enter the student identification number: ")
            print()
            name = request_name()
            print()            
            age = request_int("Enter the student's age: ")
            print()
            course = request_course()
            print()
            status = input("Enter user status (active/inactive): ").capitalize()

            add_student(list_students,id,name,age,course,status)

            print()

            print(f"Student added successfully\n")

            follow = input("Do you want to add another student? (Yes/No): ").lower()

            print()

            if follow not in ("y", "yes"):
                print("----Returning to the menu----\n".upper())
    # Show list of students           
    elif action == 2:
        print("----list of students----\n".upper())
        student_list(list_students)
        print("----Returning to the menu----\n".upper())
    # Search for student
    elif action == 3:
        print("----Search for student----\n".upper())
        
        follow = "yes"
        
        while follow in ("y", "yes"):
            
            name = request_name()
            student = search_student(list_students, name)

            if student:
                print(f"{student}\n")
            else:
                print(f"student not found\n")
            
            follow = input("Do you want to add another student? (Yes/No): ").lower()
            print()

            if follow not in ("y", "yes"):
                print("----Returning to the menu----\n".upper())
    # Update student
    elif action == 4:
            print("----Update student----\n".upper())
            
            follow = "yes"
            
            while follow in ("y", "yes"):
                
                name = request_name()
                student = search_student(list_students, name)
                
                if student is None:
                    print(f"student not found\n")

                else:
                    edit_id = input("Do you want to edit the student's id?(Yes/No): ").lower()

                    if edit_id in ("yes","y"):
                        print()
                        new_id = request_int("Enter the student's new id: ")
                        print()
                    else:
                        new_id = None

                    edit_age = input("Do you want to edit the student's age? (Yes/No): ").lower()
                    
                    if edit_age in ("yes","y"):
                        print()

                        new_age = request_int("Enter the student's new age: ")

                        print()
                    else:
                        new_age = None

                    edit_course = input("Do you want to edit the student's course? (Yes/No): ").lower()

                    if edit_course in ("yes","y"):
                        print()
                        new_course = request_course()
                        print()
                    else:
                        new_course = None

                    edit_status = input("Do you want to edit the student's status? (Yes/No): ").lower()    

                    if edit_status in ("yes","y"):
                        print()
                        new_status = input("Enter the student's new status(active/inactive): ").capitalize()
                        print()
                    else:
                        new_status = None


                    if new_id is not None or new_age is not None or new_course is not None or new_status is not None:
                        update_student(list_students,name,new_id,new_age,new_course,new_status)
                    else:
                        print("No changes were made.\n")

                follow = input("Do you want to update another student? (Yes/No): ").lower()

                print()

                if follow not in ( "y", "yes"):
                    print("----Returning to the menu----\n".upper())
    # Remove student
    elif action == 5:
            print("------Remove student------\n".upper())
            
            follow = "yes"
            
            while follow in ( "y", "yes"):
                
                name = request_name()
                
                remove_student(list_students, name)

                follow = input("Do you want to remove another student? (Yes/No): ").lower()

                print()

                if follow not in ("y", "yes"):
                    print("----Returning to the menu----\n".upper())
    # Save data to CSV files
    elif action == 6:
        print("-------Saving file-------\n".upper())

        route = input("Enter the file path (listado.csv): ")
        print()

        save_csv(list_students,route)

        print("------Returning to the menu-------\n".upper())
    # Exiting the system
    elif action == 7:
        print("Exiting the system\n")

    else:
        print("Error: Invalid option\n")