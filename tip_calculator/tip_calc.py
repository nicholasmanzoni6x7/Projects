print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip_percent = float(input("What percentage tip would you like to give? "))
payers = int(input("How many people to split the bill? "))
print("Let's see now...")
new_bill = round((bill*(tip_percent/100) + bill),2)
final = round((new_bill / payers),2)
final = "{:.2f}".format(new_bill/payers)
print(f"Each person should pay: ${final}")