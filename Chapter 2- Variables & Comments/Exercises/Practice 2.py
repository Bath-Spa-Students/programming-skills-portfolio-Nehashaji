#Write a python program that takes courses marks as input and then calculates average of all the
#courses. After calculating the average, calculate the percentage of a student using total marks. Assume
#the total of all the courses marks is 500 or take the total marks from the user as input. 

a=float(input("Enter the marks  of Math:"))
b=float(input("Enter the mark of Science:"))
c=float(input("Enter the mark of English:"))
sum=a+b+c
avg=sum/3
print("Average mark is", avg)
total_marks = float(input("Enter the total marks: "))
percentage=sum/total_marks*100
print("Your percentage is", percentage)

