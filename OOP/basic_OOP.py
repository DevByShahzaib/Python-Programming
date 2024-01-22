# OBJECT ORIENTED PROGRAMMING 
class Dog:
    def __init__(self,name,):
        self.name = name
        print(name) 
        
        

    def add_one(self,x):
        return x + 1


    def bark(self):
        print("bark")
d = Dog("shahzaib")
d2 = Dog("Khan")
d.bark()
print(type(d))

print(d.add_one(9))