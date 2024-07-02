print("Welcome to the tip calculator!") # greating
# amount to pay
amount=float(input("what is the total bill?:")) 
#tip amount
tip_amount=int(input("how much would you like to tip:"))
#number of people to split the bill
number_of_people=int(input("How many people to split the bill ?:"))
tip_amount=float(tip_amount/100)
#total amount calcilated
total_amount=float((tip_amount *amount)/number_of_people)
#output
print(f"Each person will pay : {total_amount}")