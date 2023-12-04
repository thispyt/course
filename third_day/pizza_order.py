#don't change the code bellow
print("welcome to python pizza deliveries! ")
size=input("what's size pizza do you want? S, M or L ? \n")
add_pepperoni=input("do you want pepperoni ? Y or N ? \n")
extra_cheese=input("Do you want extra cheese ? Y or N ? \n")
#don't change the code above
#write your code code below this line
# if size =="S":
#     bill=15
#     if add_pepperoni=="Y":
#         bill+=2
#         # print(f"small pizza: ${bill}")
# elif size=="M"  :    
#     bill=20
#     if add_pepperoni=="Y":
#         bill+=3
# elif size=="L" :    
#     bill=25
#     if add_pepperoni=="Y":
#         bill+=3
# if extra_cheese=="Y":
#     bill+=1
    
    
# print(f"Your final bill is: ${bill}")
#Other 
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
else:
    bill+=25

if add_pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if extra_cheese=="Y":
    bill+=1
print(f"Your final bill is: ${bill}")