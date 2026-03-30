def request_name():
    """

    Prompts the user for the student's name.

    Rules:

    - Cannot be empty.

    - Only allows letters and spaces.

    Returns:

    str: Valid name in lowercase.
    """
    name = ""
    # Loop to validate the name until it is valid
    while name == "" or not name.replace(" ", "").isalpha():
        name = input("Enter the student's name: ").capitalize()

        if name == "":
            print("Warning: Do not leave the field empty\n")
        elif not name.replace(" ", "").isalpha():
            print("Error: Only letters are allowed\n")

    return name

def request_int(massage):
    """
    Prompts the user to enter a valid integer.

    Parameters:

    message (str): Text to display.

    Returns:

    int: Valid value entered.
    """
    # Loop to validate age until correct
    valor = -1
    while valor <= 0:
        try:
            valor = int(input(massage))

            if valor <= 0:
                print("Warning: Age must be greater than 0\n")

        except ValueError:
            print("Error: Invalid entry, only numbers allowed\n")
            valor = -1

    return valor

def request_course():
    """
    Prompts the user to enter the name of the course the student is enrolled in.

    Rules:

    - Cannot be empty.

    - Only letters and spaces are allowed.

    Returns:

    str: Valid lowercase course name.
    """
    course = ""
    # Loop to validate the name until it is valid
    while course == "" or not course.replace(" ", "").isalpha():
        course = input("Enter the student's course name: ").capitalize()

        if course == "":
            print("Warning: Do not leave the field empty\n")
        elif not course.replace(" ", "").isalpha():
            print("Error: Only letters are allowed\n")

    return course

def add_student(list_students,id,name,age,course,status):
    """
    Adds a new student to the student list.

    Parameters:
        list_students (list): List of students.
        id (int): Student ID number.
        name (str): Student name.
        age (int): Available age (>= 0).
        course (str): Course name.
        status (str): Student status (active/inactive).

    Returns:
        None
    """
    student = {
        "id": id,
        "name": name,
        "age": age,
        "course": course,
        "status": status
    }
    list_students.append(student)

def student_list(list_students):
    """
    Displays all students in the console.

    Parameters:
        list_students(list): List of students.

    Returns:
        None
    """
    if not list_students:
        print("Empty student list\n")

    else:
        print("-"*70)
        print("| Id            | name        | age    | course          | status    |")
        print("|---------------|-------------|--------|-----------------|-----------|")
        for s in list_students:
            print(
                f"| {s['id']:<13} | {s['name']:<11} | {s['age']:<6} | {s['course']:<15} | {s['status']:<9} | "
            )
        print("-"*70)

def search_student(list_students, name):
    """
    Searches for a student by name in the student list.

    Parameters:
        list_students(list): List of students.
        name (str): Name of the student to search for.

    Returns:
        dict: Student found.
        None: If the student does not exist.
    """
    for s in list_students:
        if s["name"].capitalize() == name:
            return s
    return None

def update_student(list_students,name,new_id=None,new_age=None,new_course=None,new_status=None):
    """
    Update the information of an existing student.

    Parámetros:
        list_students(list): List of students.
        
        name (str): Name of student to be updated.
        list_students(list): List of students.
        name (str): Name of student to be updated.
        new_id (int, optional): New id.
        new_name (str): new name.
        new_age (int, optional): New age.
        new_course (str, optional): New course.
        new_status(str, optional): New status.

    Return:
        None
    """
    student = search_student(list_students,name)
    
    if student is None:
        print("student not found\n")
        return 
    
    if new_id is not None:
        student["id"] = new_id

    if new_age is not None:
        student["age"] = new_age     

    if new_course is not None:
        student["course"] = new_course

    if new_status is not None:
        student["status"] = new_status

    print("Student updated correctly\n")

def remove_student(list_students, name):
    """
    Removes a student from the list.

    Parameters:
        list_students(list): List of students.
        name (str): Name of the student to remove.

    Return:
        None
    """
    student = search_student(list_students,name)

    if student:
        list_students.remove(student)
        print("student successfully removed\n")
    else:
        print("student not found\n")