print("welcome to Treasure Island.\nYour mission is to find the treasure ")
direction=input('You\'re at a cross road. Where do you want to go? type "left" or "right"')
if direction=="left":
    how_to_go=input('you come to a lake. there is an island in the middle of the lake. type to "wait" to wait for a boat. type "swim" to swim across ?')
    if how_to_go=="wait":
        which_door=input("you arrive at the island unharmed. there is a house with 3 doors. one red ,one yellow and one blue which color do you choose?")
        if which_door=="yellow":
            print("You win!")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over.")