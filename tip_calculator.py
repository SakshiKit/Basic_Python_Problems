print("Welcome to the tip calculator!")
bill = (int(input("What was your total bill ?")))
print(bill)
tip = (int(input("How much tip would you like to give? 10, 12, or 15?")))
print(tip)
div = (int(input("How many people to split the bill?")))
print(div)
tip_as_percent = tip / 100
total_amount = bill * tip_as_percent
total_bill = bill + total_amount
final_amount = round(total_bill / div, 2)
print(f"Each person should pay: {final_amount}")