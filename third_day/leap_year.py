year=int(input("which year do you want to check?"))
if year%4==0 and year%400==0:
    print(f"cette annee {year} est bisextille ")
else:
    print(f"cette annee {year} n'est pas bisextille ")
    

