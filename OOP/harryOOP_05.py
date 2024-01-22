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
    

    @classmethod #decorator
    def change_increment(cls, amount):
        cls.increment = amount


    @classmethod
    def from_str(cls, emp_str):
        fname, lname, salary = emp_str.split("-")
        return cls(fname,lname,salary)



    
lovish = Employee.from_str("Shahzaib-Khan-80000")
print(lovish.fname,lovish.lname)
# harry = Employee("Shahzaib", "Khan", 80000)
   
# rohan = Employee('Rafay', 'khan', 80000)
# Employee.change_increment(3)
# harry.increase()
# print(harry.salary)  

