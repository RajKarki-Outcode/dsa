def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >=75:
        return 'B'
    elif score >= 50:
        return 'C'
    else:
        return 'F'
    

students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        score = float(input("Enter marks out of 100: "))
        students[name] = score
        print(f"Student added!")
    
    elif choice == '2':
        if not students:
            print("No students found.")
        
        else:
            print("\nStudents:")
            for name, score in students.items():
                grade = get_grade(score)
                print(f"{name.title()}: {score} - Grade: {grade}")

    elif choice == '3':
        name = input("Enter student name to search: ")
        if name in students:
            score = students[name]
            grade = get_grade(score)
            print(f"{name.title()}: {score} - Grade: {grade}")
        else:
            print("Student not found.")
    elif choice == '4':
        name = input("Enter student name to update: ")
        if name in students:
            score = float(input("Enter new marks out of 100: "))
            students[name] = score
            print(f"Student {name.title()} updated!")
        else:
            print("Student not found.")
    elif choice == '5':
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print(f"Student {name.title()} deleted!")
        else:
            print("Student not found.")
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
