# TODO
mini=5
normal=8
large=10
mushroom_mini_normal=1
mushroom_large=2
extraCheese=1
total=0
print("Welcome to Burger House")
print("Burger House Menu")
print("Mini Burger (M): $5")
print("Normal Burger (N): $8")
print("Large Burger (L): $10")
print("Add mushroom for Mini and Normal = $1, For Large = $2")
print("Extra Cheese = $2")

size=input("Which size of burger you want?")
if size==str("M"):
    total=total+mini
    add_mushroom=input("Do you want to add mushroom? Y/N")
    if add_mushroom==str("Y"):
        total=total+mushroom_mini_normal
elif size==str("N"):
    total=total+normal
    add_mushroom=input("Do you want to add mushroom? Y/N")
    if add_mushroom==str("Y"):
        total=total+mushroom_mini_normal
elif size==str("L"):
    total=total+large
    add_mushroom=input("Do you want to add mushroom? Y/N")
    if add_mushroom==str("Y"):
        total=total+mushroom_mini_normal

else :
    print("Please enter your choice in M/N/L to place an order.")

cheese=input("Want to add extra cheese? Y/N")
if cheese==str("Y"):
    total=total+extraCheese

print(f"Your final bill is: $ {total}")
    
    

