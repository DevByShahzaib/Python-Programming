class Fraction:
    def __init__(self,x,y):
        self.num = x
        self.den = y
        
    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self,other):
     d = self.den * other.den
     n = (self.num*other.den)+(self.den*other.num)
     return Fraction(n,d)

f1 = Fraction(5,11)
f2 = Fraction(2,9)
f3 = f1 + f2
print(f3)
        
       