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


    
harry = Employee("Shahzaib", "Khan", 80000)
   
rohan = Employee('Rafay', 'khan', 80000)
Employee.change_increment(2)
harry.increase()
print(harry.salary)  
