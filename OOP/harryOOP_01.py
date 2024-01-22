class Employee:
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        
    
    
harry = Employee("Shahzaib", "Khan", 80000)
rohan = Employee('Rafay', 'khan', 80000)

print(harry.fname)