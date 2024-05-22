print("Welcome to the love calculator!")
name1=str(input("Enter your name: "))
name2=str(input("Enter lover name: "))
combined_name=name1+name2
name=combined_name.lower()
# for counting TRUE in name
t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")

true=t+r+u+e

# for counting LOVE in name
l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")

love=l+o+v+e
# concatenating both true and love
lovescore=str(true)+str(love)
lovescore=int(lovescore)
# applying condition 
if lovescore<10 or lovescore>85:
    print(f"Your love score is {lovescore}, you go together like Coke and Mentos.")
elif lovescore>=40 and lovescore<=70:
    print(f"Your love score is {lovescore}, you are alright together.")
else:
    print(f"Your love score is {lovescore}.")





