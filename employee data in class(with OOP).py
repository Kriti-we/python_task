# main class
class Person():
    def __init__(self, per_name, per_designation):
        self.name = per_name
        self.designation = per_designation
	
    def display1(self):
        print("name:", self.name)
        print("designation:", self.designation)

# subclass		
class Employee(Person):
    def __init__(self, emp_name, emp_designation, emp_salary):
        self.salary = emp_salary
        super().__init__(emp_name, emp_designation)
	
    def display2(self):
        print("salary:", self.salary)
        super().display1()
		
emp = Employee("Rushil","Graphic Desinger", 35000)  

emp.display2()