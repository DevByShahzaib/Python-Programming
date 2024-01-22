# To find prime number
num = int(input('enter your prime num and we will corect it :'))
prime = True
for i in range(2, num):
    if num%i == 0:
        prime = False
        break
if prime:
    print('this is prime number..')    
else :
    print('this is not a prime number..')    