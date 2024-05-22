a=input("Enter the Starting Number: ")
b=input("Enter the Ending Number: ")

i=int(a)
j=int(b)
if i==j:
    print("Please mention the gap between starting and ending number: ")
else :
    if i>j:
            print("Ending Number is greater than starting number: ")
    else:
            while i<=j:
                print(i)
                i=i+1
