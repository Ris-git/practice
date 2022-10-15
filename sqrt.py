salary = int(input("Enter your current salary: "))
service = int(input("Enter your year of service: "))
if service > 5:
    print("The net bonus amount is Rs :", salary + 1000)
else:
    print("The bonus is not applicable to you.")    