class Employee:

    increment = 1.5
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname= lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * Employee.increment) 

    #here we use class method
    @classmethod
    def change_salary(cls, amount):
        cls.increment = amount

    @classmethod
    def classconstructor(cls, str_arg):
        fname, lname, salary =    str_arg.split('-')
        return cls(fname, lname, salary)

    @staticmethod
    def isopen(day):
        if day == "sunday":
             return False
        else:
            return True

print(Employee.isopen("sunday"))
# lovish = Employee.classconstructor("shahzaib-khan-80000")
# print(lovish.salary)
# print(lovish.fname)
# print(lovish.lname)
# shahzaib = Employee("Shahzaib", "Khan" , 80000)
# sufyan = Employee("Sufyan", "Khan", 80000 )
# print(shahzaib.salary)
# shahzaib.increase()
# print(shahzaib.salary)
# print(shahzaib.__dict__)# for all variables

# print(shahzaib.salary)
# Employee.change_salary(2)
# shahzaib.increase()
# print(shahzaib.salary)
