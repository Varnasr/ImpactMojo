name = input("What is your name? ")
age = int(input("How old are you? "))

yearsto50 = 50 - age

if yearsto50>0:
    print("Hello " + name.title() +", you will be 50 in "+ str(yearsto50)+ " years")
else:
    print("Hello "+ name.title() +", you were 50 "+ str(-yearsto50)+ " years ago.")

print("bye")