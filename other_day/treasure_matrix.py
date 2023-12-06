row1 =["😊","😊","😊"]
row2 =["😊","😊","😊"]
row3 =["😊","😊","😊"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
# print(map)
position=input("where do you want to put the treasure? \n")
# tolist=list(position)
horizantal=int(position[0])
vertical=int(position[1])
column=map[vertical-1]
column[horizantal-1]="X"
# print(map)
print(f"{row1}\n{row2}\n{row3}\n")
