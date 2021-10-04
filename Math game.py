num1 = int(input("Enter the first whole number: "))
num2 = int(input("Enter the second whole number: "))
print("Enter 1 to ADD")
print("Enter 2 to SUBTRACT")
print("Enter 3 to MULTIPLY")
choice = int(input())
if choice == 1:
    print(num1 + num2)
else:
   if choice == 2:
     print(num1 - num2)
   else:
       if choice == 3:
           print(num1 * num2)
       else: choice > 3
       print("Follow the rules >:(")
