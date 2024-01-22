# T1 = (1, 4, 7, 2, 9, 3) #tuple can't be change
# t1= (1,)#tuple with single element

marks1 = int(input('enter you marks::'))
marks2 = int(input('enter you marks::'))
marks3 = int(input('enter you marks::'))
if (marks1>33):
    print(' you are passed in subject-1...')
else :
    print(' sorry bro you are FAIL in subject-1...')    
if (marks2>33):
    print(' you are passed in subject-2...')
else :
    print(' sorry bro you are FAIL in subject-2...')
if (marks3>33):
    print(' you are passed in subject-3...')
else :
    print(' sorry bro you are FAIL in subject-3...')
if (marks1+marks2+marks3)>120:
    print('you are passed')
else:
    print('you are FAILED')