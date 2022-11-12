a=float(input("Enter any numer :"))
b=float(input("Enter any number :"))
opr=str(input("Which operation do you want to perform :"))
def cal(a, b, opr):
    if opr == '+':
        print( a + b)
    elif opr == '-':
        print( a - b)
    elif opr == '*':
        print( a * b)
    elif opr == '/':
        print(a / b)
    else:
        print("None")


cal(a,b,opr)


    