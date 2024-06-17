print("Thank you for choosing Python Pizza Deliveries!")
size = input("enter the size S,M or L?")
print(size)
add_pepperoni = input("do you want pepperoni Y or N?")
print(add_pepperoni)
extra_cheese = input("do you want extra cheese Y OR N ?")
print(extra_cheese)

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

