fruits=["Peach","Apple","pear"]
for fruit in fruits:
    print(fruit)
#exercise Average Height:

student_heights=[180,124,165,173,189,169,146]
# lenght=len(student_heights)
#not use len() and sum()
sum_students=0
i=0
for students_height in student_heights:
    sum_students += students_height
    i+=1    
average=sum_students/i
print(round(average))
std_hgt=input("input a list of student heights ").split()
for n in range(0,len(std_hgt)):
    std_hgt[n]=int(std_hgt[n])
print(std_hgt)
sum_students=0
index=0
for nn in std_hgt:
    sum_students+=nn
    index+=1
aver=sum_students/index
print(round(aver))
lenght_student=len(std_hgt)
sum_student=sum(std_hgt)
average_height=round(sum_student/lenght_student)
print(average_height)