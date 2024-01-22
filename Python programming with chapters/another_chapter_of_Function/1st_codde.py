def myFunction(marks):
    p = (sum(marks)/400)*100
    return p



marks1 = [55, 66, 77, 88, 99]
percentage1 = myFunction(marks1)



marks2 = [55, 66, 57, 58, 99]
percentage2 = myFunction(marks2)
print(percentage1,percentage2)