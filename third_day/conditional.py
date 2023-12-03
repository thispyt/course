# # if condition:
# #   do this
# # else:
# #   do this
# #restroom
# water_level=50
# if water_level>80:
#     print("drain water")
# else:
#     print("continue")
# #ticket for enjoy in the rollercoaster ?
# # flowshard  draw.io
# print("Welcome to the rollercoaster!")
# height=int(input("what's your height in cm ?"))
# if height>120:
#     print("can ride the rollercoaster, your tall enough ")
# else:
#     print("Sorry, you have to grow taller before you ride the rollercoaster")
# #exercise odd or even
# print("Welcome to the calculator of odd or even")
# number=int(input("Entre a number"))
# if number%2==0:
#     print(f"number {number} is even")
# else :
#     print(f"number {number} is odd")
# #other
# #don't change the below code
# print("Welcome to the calculator of odd or even")
# number_as=int(input("which number do you want to check"))
# #don't change the above code
# #write your code bellow this code
# # number=int(input("Entre a number"))
# if number%2==0:
#     print(f"number {number} is even")
# else :
#     print(f"number {number} is odd")
# #Modulo Operation % > 7%2 -> 7=2+2+2+1 result is 1,
# # 7%3= '3*3'+1=1 
# #6%2=3*'2'+0=0 , 14%4 =3*4(4->2*2)+2=2 ,5/2= 2*2+1=1
# ########
# #Nested if statements and else if statements
# #if condition:
# #   if anothercondion :
# #       do this
# #   else:
# #       do this
# #else
# #   do this
# print("Welcome to the rollercoaster!")
# height=int(input("what's your height in cm ?"))
# if height>120:
#     print("can ride the rollercoaster, your tall enough ")
#     age=int(input("what's your age"))
#     if age>18:
#         print("you should be pay : $12")
#     else:
#         print("you should be pay : $7")
# else:
#     print("Sorry, you have to grow taller before you ride the rollercoaster")
print("Welcome to the rollercoaster!")
height=int(input("what's your height in cm ?"))
if height>120:
    print("can ride the rollercoaster, your tall enough ")
    age =int(input("write your age"))
    if age<12:
        bill=5
        print("please pay : $5")
    elif age>=12 | age<=18:#or age<=18 just
        bill=7
        print("please pay : $7")
    else:
        bill=12
        print("please pay : $12")
    wants_photo=input("Do you want a photo taken? Y or N. \n")
    if wants_photo=="Y":
        bill+=3
        
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you ride the rollercoaster")
