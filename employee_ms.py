class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}"


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, emp_id, department):
        new_employee = Employee(name, emp_id, department)
        self.employees.append(new_employee)
        print(f"Employee '{name}' added successfully.")

    def show_employees_in_department(self, department):
        print(f"\nEmployees in the '{department}' department:")
        found = False
        for emp in self.employees:
            if emp.department.lowr() == department.lower():
                print(emp)
                found = True
        if not found:
            print(f"No employees found in the '{department}' department.")

    def list_all_employees(self):
        print("\nAll employees:")
        if not self.employees:
            print("No employees have been added yet.")
        else:
            for emp in self.employees:
                print(emp)
