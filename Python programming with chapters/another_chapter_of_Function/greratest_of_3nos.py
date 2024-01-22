#find greatest of three numbers....
num1 = int(input('enter your number:::'))
num2 = int(input('enter your number:::'))
num3 = int(input('enter your number:::'))
def Greatestnos(num1,num2,num3):
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
print(Greatestnos(num1,num2,num3))            
                    