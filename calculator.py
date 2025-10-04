print("Welcome to tip Calculator")

n = int(input("what is your total amount?"))

t = int(input("how much tip would you like to give?"))
total = 0
if t > n :
    print("Only 100% tip is allowed")
else:
    tip = n * t//100
    total = tip + n

p = int(input("How many people to split the bill?"))

s  = total / p
print("Your total amount is:",s)




