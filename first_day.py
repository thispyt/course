#print a string into the console
print("Welcome")
#print a string into the console, and asks the user for a string input
name = input("What's your name ")
#print variable
print(name)
# A variable give a name to a piece of data.
# like a box with a label, it tells you what's inside the box 
my_name="paassaas"
my_age=22
#the += Operator , this is a convient way of saying:
#take the previous value and add to it
my_age+=2
print(my_age)
#F-STRINGS You can insert a variable into a string using f-string 
#The syntaxe is simple, just insert the variable in-between a set of curly braces {}.
days=365
print(f"there are {days} in a year ")
#Converting Data type 
#You can convert a variable from 1 data type to another
# to float,int,string float(),int(),str()
print(float(days))
floa=3.4
print(int(floa))
print(str(days))
#Checking Data types
print(type(days))
print(type(floa))
print(type(my_name))