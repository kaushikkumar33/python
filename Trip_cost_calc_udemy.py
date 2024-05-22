print("Welcome to the trip cost calculator!\n")
#Trip cost calculator project of udemy!!
stay=int(input("How many days will you stay?\n"))
hotelCost=float(input("How much does hotel cost per night?\n"))
flight=float(input("How much does flight cost?\n"))
rentalCar=float(input("Do you need rental car?\nIf Yes type 1 \nIf no type 0\n"))
others=float(input("Enter other possible expenses:\n"))


rent=0
if rentalCar==1:
    rent=stay*10

expense=stay*hotelCost + flight + others+ rent
print("Total Cost = $" ,round(expense,2))


