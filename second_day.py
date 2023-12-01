#Data types,String,index for printing position char [subscript]
print("hello"[2])#display char l
print("1234"[0])#display first number or char 1
#concat number after add
print("123"+"456")
print(123+456)#integer addition
#float ,bool
print(3.35)
print(True)
print(False)
#len function for string not integer (TypeError int has no len) for below display 5
print(len("hello"))
#Type checking and conversation
# num_char=len(input("what's your name"))
# print("your name has "+ num_char+" character.")
#TypeError: can only concatenate str (not "int") to str 
# solution is parse(conversation [integer to string ]), follow in below 
#type value in num_char is integer number of character
num_char=len(input("what's your name \n"))
new_num_char=str(num_char)
#a integer number between two string  Error: can only concatenate str (not "int") 
print("your name has "+ new_num_char+" character.")
#but print("your name has "+ new_num_char) not

a=float(123)#conversing int to float like 123.0
print(type(a))#determine type of variable
print(70+a)#display addition resylt float
print(str(70)+str(100))#just concating two string
#exercise
# Write a program that adds in a 2 digit number. e.g.
#the input was 35,then the output should be 3+5=8
#mY practice 
digit=input("write 2 digit number")
#by default type of input is string you should be parse or conserv 3la hsab haja 
# print(type(digit)
add=int(digit[0]) + int(digit[1])
print(add)
# print("result is "+str(add))# ERROR AVIODANCE
#other practice
# Don't change the code below
two_digit_number=input("type a two digit number")
#don't change the code above
#write your code below this line
first_digit=two_digit_number[0]
second_digit=two_digit_number[1]
result=int(first_digit)+int(second_digit)
print(result)
#Mathematical operations in python like PEMDAS(LR?)
#P as parallele (), E as Exponnent ** , M multiplication number * number
#D divition / , A Addition, S substracting 
print(3*3+3/3-3)#not P and E display 3*3=9 , 3/3=1.0 ,9+1=10.0 ,10.0 -3 =7.0
print(3*(3+3)/3-3)# P (A)3+3=6,E not exist,M 3*6=18, D 18/3=6.0 ,S 6.0 -3=3.0