sales = float(input("Enter the Generated Sales or -1 to stop: "))

while sales != -1
    comm_rate = float(input("Enter commision rate: "))

    while comm_rate < 0.15 or comm_rate > 0.25:
        print("Invalid entry.\n Must be between 0.15 or 0.25")
        comm_rate = float(input("Please enter commision rate again"))

    
    comm = sales * comm_rate
    print(comm)

    sales = float(input("Enter the Generated Sales or -1 to stop: "))
