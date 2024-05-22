# this program is for gross pay with or without overtime.
# if work hour is below or equal to 40 then no over time is calculated.
try:
    hour=float(input("Enter the Hour: "))
except:
    print("Please Enter Numeric Value.")
    # hour=float(input("Enter the Hour: "))
    quit() #quit use for exit from the program.
    
try:
    rate=float(input("Enter the rate: "))
except:
    print("Please Enter Numeric Value.")
    # rate=float(input("Enter the rate: "))
    quit()
over_time=0
pay=0
if hour<=40:
    pay=round(hour*rate,2)
    print(f"Your net pay is {pay}")
else:
    over_time=hour-40
    pay=round(40*rate + over_time*1.5*rate,2)
    print(f"Your net pay with {over_time} hour overtime is {pay}")

