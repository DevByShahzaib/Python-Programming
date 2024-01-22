class Employee:
    increment = 1.5
    no_of_Employee = 0
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_Employee +=1
        
    def increase(self):
        self.salary = self.salary * self.increment
    

print(Employee.no_of_Employee)    
harry = Employee("Shahzaib", "Khan", 80000)
print(Employee.no_of_Employee)    
rohan = Employee('Rafay', 'khan', 80000)
print(Employee.no_of_Employee)    
sam = Employee('Afridi', 'khan', 80000)
print(Employee.no_of_Employee)    

# print(harry.fname)
# print(harry.__dict__)
# print(Employee.__dict__)