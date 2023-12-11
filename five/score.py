# students_score=input("wtire the scores of studens").split()
# students_list=list(students_score)
# for student in students_list:
#     print(student)
students_score=input("wtire the scores of studens").split()
max=0
for n in range(0,len(students_score)):
    students_score[n]=int(students_score[n])
    # max=students_score[n]
    if max <students_score[n]:
        max = students_score[n]
print(f"The highest score in the class is: {max}")
# for comp_student in students_score:
#     max=stu
# print(students_score)
    