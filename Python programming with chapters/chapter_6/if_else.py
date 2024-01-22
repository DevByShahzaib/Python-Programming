# #greatest of 6 number...
# num1 = int(input('Enter your number:::'))
# num2 = int(input('Enter your number:::'))
# num3 = int(input('Enter your number:::'))
# num4 = int(input('Enter your number:::'))
# num5 = int(input('Enter your number:::'))
# num6 = int(input('Enter your number:::'))
# if num1>num2:
#     f1 = num1
# else :
#     f1 = num2
# if num3>num4:
#     f2 = num3
# else :
#     f2 = num4
# if num5>num6:
#     f3 = num5
# else :
#     f3 = num6
# if f1>f2:
#     f4=f1
# else:
#     f4=f2
# if f4>f3:
#     print(f'{f4} is the greatest number...')
# else:
#     print(f'{f3} is the greatest number...')
    

marks1 = int(input('enter you marks::'))
marks2 = int(input('enter you marks::'))
marks3 = int(input('enter you marks::'))
if (marks1>33):
    print(' you are passed in one subject...')
else :
    print(' sorry bro you are FAIL in one subject...')    
if (marks2>33):
    print(' you are passed in one subject...')
else :
    print(' sorry bro you are FAIL in one subject...')
if (marks3>33):
    print(' you are passed in one subject...')
else :
    print(' sorry bro you are FAIL in one subject...')
if (marks1+marks2+marks3)>120:
    print('you are passed')
else:
    print('you are FAILED')