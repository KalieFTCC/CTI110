foodPrice = float(input("Enter the price of food: "))
tip = float(input("Enter the Tip percent you want to use: "))
if tip ==0:
    tip = 20
else:
    print("Alright, i'll get right on that")
tip = tip / 100
tip = foodPrice * tip
foodPrice = tip + foodPrice
print("Your foods total price is: " , foodPrice)
