print("Welcome to Lund Pizza Delevries!")
total = 0
size = input("What size pizza do you want? S, M, or L: ")

if size == "S" or size == "s":
    total += 20
elif size == "M" or size == "m":
    total += 40
elif size == "L" or size == "l":
    total += 50
else:
    print("Invalid input, please try again.")
    exit()

pepperoni = input("What do you want pepperoni? Y or N:")

if pepperoni == "Y" or pepperoni == "y" :
    total += 2
elif pepperoni == "N" or pepperoni == "n":
    total = total
    print("No Pepperoni")
else:
    print("Invalid input, please try again.")
    exit()

cheese = input("What do you want cheese? Y or N:  ")
if cheese == "Y" or cheese == "y":
    total += 2
elif cheese == "N" or cheese == "n":
    total = total
    print("No cheese")
else:
    print("Invalid input, please try again.")
    exit()


print("your total bill is $ {}".format(total))
