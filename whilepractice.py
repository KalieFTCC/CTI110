keep_going = "y"

while keep_going == "y":
    sales = float(input("Enter Sales: "))
    comm_rate = float(input("Enter commision rate: "))
    comm = sales * comm_rate
    print(comm)

    keep_going = input("Do you want to calculate another commission?/n (y/n: )")
