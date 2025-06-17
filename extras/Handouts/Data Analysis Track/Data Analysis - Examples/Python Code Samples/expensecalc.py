exp = -1
total = 0
maxexp = 0
minexp = 0

while exp!=0:
    exp = int(input("What is the expense? (type 0 to stop) "))
    total = total + exp
    if exp>maxexp:
        maxexp = exp
print("Your total expenditure is " + str(total))
print("The maximum you spent is " + str(maxexp))