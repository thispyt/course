print("Welcome to the tip calculator.")
# total_bill=input("what was the total bill? $ ")
# type_perce=input("what parcentage tip would you like to give? 10 ,12 or 15? ")
# number_people_split=input("how many people to split bill ")

# pay=(float(total_bill) / int(number_people_split))*((float(type_perce)/100)+1)
# print(pay)
bill=float(input("what was the total bill? $"))
tip=int(input("what much tip would you like to give? 10,12 15 ?"))
people=int(input("how many people to split bill"))
tip_as_perce=tip/100
total_tip_amount=bill*tip_as_perce
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
print(f"Each person should pay : ${final_amount}")
# Étape 1: Demander à l'utilisateur le montant total de la facture
bill = float(input("What was the total bill? $"))

# Étape 2: Demander à l'utilisateur le pourcentage de pourboire qu'il souhaite donner (10%, 12%, 15%, etc.)
tip = int(input("How much tip would you like to give? 10, 12, 15?"))

# Étape 3: Demander à l'utilisateur le nombre de personnes pour diviser la facture
people = int(input("How many people to split the bill?"))

# Étape 4: Convertir le pourcentage de pourboire en une valeur décimale
tip_as_percentage = tip / 100

# Étape 5: Calculer le montant total du pourboire en multipliant le montant de la facture par le pourcentage de pourboire
total_tip_amount = bill * tip_as_percentage

# Étape 6: Calculer le montant total de la facture en ajoutant le montant de la facture au montant total du pourboire
total_bill = bill + total_tip_amount

# Étape 7: Calculer le montant à payer par personne en divisant le montant total de la facture par le nombre de personnes
bill_per_person = total_bill / people

# Étape 8: Arrondir le montant à payer par personne à deux décimales
final_amount = round(bill_per_person, 2)

# Étape 9: Afficher le montant à payer par personne
print(f"Each person should pay: ${final_amount}")
