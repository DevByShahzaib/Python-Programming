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

    @staticmethod #independent function...
    def isopen(day):
        if day=='sunday':
            return False
        else:
            return True

class programmer(Employee):
    def __init__(self, fname, lname, salary,proglang, exp):
        super().__init__(fname, lname, salary)
        self.proglang = proglang 
        self.exp =  exp

  
shahzaib = programmer("shahzaib", "Khan","90000",'JavaScript', '2 yrs')
print(shahzaib.exp)
