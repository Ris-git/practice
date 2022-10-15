X = int(input("Enter your current salary: "))
Y = int(input("Enter the time spent on company: "))
if Y >= 10:
    print("Your net bonus is " , X + X * 10/100)
elif Y >= 6 and Y < 10:
    print("Your net bonus is" , X + X * 8/100)
elif Y < 6:
    print("Your net bonus is " , X + X * 5/100)
else:
    print("Sorry! no bonus for you.")            

