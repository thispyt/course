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