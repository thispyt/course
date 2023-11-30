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
#exercice print 
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
#return ligne with use \n
print("hello\nwelcome\neveryone")
#conctantion , String manipulation 
#Vscode use Code intelligence for detecte error while write code
print("hello"+" world")# Space before print indintation error 
# one qoates not exist return syntaxe error EOL \ 
# debuging error ligne after ligne (block)?
# debug :or look evenmets in the code step by step with use  app thonny

#asks your name and print hello with your name  
# first in the console input after print with entree
print("hello "+ input("what's your name"))
#save the data and print or affect data in variable or deplace in case in memory
name = input("what's your name \n")
print(f"hello {name}")
#respect order and print after lenght 
name='jack';print(f"hello {name}")
print(len(name))

#Don't change the code below
a = input("a:")
b = input("b:")
#don't change the code above
############################
#Write your code below this line
#change with help another variable
moyen=a
a=b
b=moyen
#write your code above this line
#Don't change the code below
print("a = " + a)
print("b = " + b)
#don't change the code above

#Variable Naming error space and begin with number ..
#project easy band generator
print("Welcome to the band Name Generator.")
city_grew=input("What's the name of the city you grew up in?\n")
pets_name=input("What's your pet's name?\n")
print(f"Your band name could be {city_grew} {pets_name}")
# above use f-string and or print("Your band name could be"+city_grew+" "+pets_name)