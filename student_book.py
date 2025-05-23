# Program to store student data and retrieve marks by name

def add_students():
    students = {}
    n = int(input("How many students do you want to add? "))
    
    for _ in range(n):
        student_name = input("Enter the name of the student: ").strip()
        student_marks = float(input(f"Enter the marks for {student_name}: "))
        students[student_name] = student_marks
    
    return students

def query_student_marks(students):
    while True:
        search_name = input("\nType a student's name to view their marks (or type 'quit' to stop): ").strip()
        if search_name.lower() == 'quit':
            break
        elif search_name in students:
            print(f"{search_name} has scored: {students[search_name]}")
        else:
            print(f"Sorry, no record found for {search_name}.")

# Main execution
if __name__ == "__main__":
    print("Welcome to the Student Marks Tracker!")
    student_records = add_students()
    print("\nAll records have been saved.")
    query_student_marks(student_records)
    print("Thank you for using the tracker!")
