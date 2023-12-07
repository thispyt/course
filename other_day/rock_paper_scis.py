import random as rd
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image=[rock,paper,scissors]
choose_user=int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choose_computer=rd.randint(0,2)
print(f"choose computer is : {choose_computer}")
if choose_user<0 and choose_user>2:
    print("invalid")
    
print(f"choice user{game_image[choose_user]}")

print(f"choice compt{game_image[choose_computer]}")
if choose_user ==0 and choose_computer==2:
    print("you win ")
elif choose_computer==0 and choose_user==2:
    print("you lose")
elif choose_computer > choose_user:
    print("you lose")
elif choose_user >choose_computer:
    print("you win")
else:
    print("equal")
# if (number_for_choose==2) and (num_comp==1):
#     print("you win")
# elif number_for_choose==2 and num_comp==0:
#     print("you lose")
# elif number_for_choose==1 and num_comp==0:
#     print("you win")
# elif number_for_choose==1 and num_comp==2:
#     print("you lose")
# elif number_for_choose==0 and num_comp==2:
    # print("you win")
# elif number_for_choose==0 and num_comp==1:
    # print("you lose")
# else:
    # print("equal")