import random as rd
lists_symbols=["~","!","@","#","$","%","^","&","*","(",")","_","-","=","+","`","/",";",":",'"',"'",".","?",">","<","{","}","[","]","|",""]
lists_numbers=[1,2,3,4,5,6,7,8,9,0]
lists_letters=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
# lists_symbols=["~","!","@","#","$","%","^","&","*","(",")","_","-","=","+","`","/","'\'"]
# print(lists_symbols)
# print(lists_letters)
# print(lists_numbers)
print("Welcome to the PyPassword Generate By me !")
choice_num_letter=int(input("How many letters would you like in your password?\n"))
symbole_num=int(input("How many symbols would you like?\n"))
num_num=int(input("How many numbers would you like?\n"))
# listss=str(lists_letters)
total_letter=""
for index_letter in range(0,choice_num_letter):
    total_letter=rd.randint(int(lists_letters))