import random as rd
# names=list(input("give your names"))
# name=rd.randint()
#split string method
names_string=input("give me everybody's names, seperated by a comma. ")
namess=names_string.split(", ")
print(namess)
# namess=list(namess)
x=len(namess)
y=rd.randint(0,x-1)
names_pay=namess[y]
print(y)
print(f"pay {names_pay}")