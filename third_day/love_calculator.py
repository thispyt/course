print("Welcome to the Love Calculator!")
name=input("what's your name?\n")
name2=input("what's their name?\n")
names=name+name2
true=0
love=0
true+=names.count('t')
true+=names.count('r')
true+=names.count('u')
true+=names.count('e')

love+=names.count('l')
love+=names.count('o')
love+=names.count('v')
love+=names.count('e')
score=str(true)+str(love)
# print(score +"%")
score_as_int=int(score)
if score_as_int<10 or score_as_int>90:
    print(f"Your score is {score}%, you go together like coke and mentos")
elif score_as_int>=40 and score_as_int<=50:
    print(f"Your score is {score}%, you are alright together")
else:
    print(f"Your score is {score}%")
    
