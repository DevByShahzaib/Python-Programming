# find a factorial of a given number...
num = int(input('enter your number :'))
factorial = 1
for i in range(1, num+1) :
    factorial = factorial*i
print(f'the factorial of {num} is {factorial}')

