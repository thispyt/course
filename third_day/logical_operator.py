print("Welcome to the rollercoaster!")
height=int(input("what's your height in cm ?"))
if height>120:
    print("can ride the rollercoaster, your tall enough ")
    age =int(input("write your age"))
    if age<12:
        bill=5
        print("please pay : $5")
    elif age<=18:#or age<=18 just
        bill=7
        print("please pay : $7")
    elif age >=45 and age <=55:
        print("Everthing is going to be ok. have a free ride on us ")
    else:
        bill=12
        print("please pay : $12")
    wants_photo=input("Do you want a photo taken? Y or N. \n")
    if wants_photo=="Y":
        bill+=3
    print(f"Your final bill is ${bill}")
        
