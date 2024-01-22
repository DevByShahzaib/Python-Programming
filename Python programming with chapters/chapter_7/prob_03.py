# #sum of frist n natural number is...
i = 1 
sum = 0
n = int(input('enter the number :'))
for i in range(1, n+1):
    sum = sum + i 
print(f'the sum of first{n} natural number is {sum}')
 



# solve aobve question using while loop 
i = 1 
sum = 0
n = (int(input("Enter the number: ")))
while (i<=n):
    sum += i
    i+=1
    print(f"The sum of first {n} natural number is {sum}")