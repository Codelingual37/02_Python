print("Tip Calculator (Tip your server!)")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, 15, 20? "))
people = int(input("How many people to split the bill? "))
total_bill = f"Total bill: {round((bill + (bill * (percentage / 100))), 2)}"
ind_tip = f"Your tip comes out to: {round(((bill / people) * (percentage / 100)), 2)} per person."
split_pay = f"Each person pays: {round((total_bill / people), 2)}"

print(total_bill)
print(ind_tip)
print(split_pay)
