# checking score between 0 to 1 and grade accordingly
print("Welcome to score checker!")
try:
    score=float(input("Enter the Score: "))
except:
    print("Error, Please Enter number between 0.00-1.00!")
    score=float(input("Enter the Score: "))
# try:
if score<=1:
    if score>=0.9:
        print("Grade A")
    elif score>=0.8:
        print("Grade B")
    elif score>=0.7:
        print("Grade C")
    elif score>=0.6:
        print("Grade D")
    elif score>=0.5:
        print("Grade E")
    else:
        score<0.5
        print("Fail")
else:
    print("Error, Please Enter number between 0.00-1.00!")
    quit()
        
# except:
#     print("Error, Please Enter number between 0.00-1.00!")
#     quit()


