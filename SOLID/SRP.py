#The Single Responsibility Principle (SRP) states that a class should have only one reason to change. 
#This means that a class should have only one responsibility.

#First Program -----violation of SRP
#Here, employee details,salary calculation, and save employee details is all available in one class "Employee"
#violating SRP

class Employee:
    def employee_details(self):
        name = input("Enter the employees name : ")
        age = int(input("Enter the employees age : "))
        salary = float(input("Enter the employees salary : "))
        return {"name": name, "age":age,"salary":salary}       

    def  salary_calculation(self,salary):
        print(f"Salary is {salary}")

    def save_employee_details(self, employee):
        with open("SOLID/employees.txt", "a") as file:
            file.write(f"Name: {employee['name']}, Age: {employee['age']}, Salary: {employee['salary']}\n")      

e=Employee()
employeedetails=e.employee_details()
e.save_employee_details(employeedetails)