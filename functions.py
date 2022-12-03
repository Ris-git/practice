
# def mutiply(x ,y):
#     output = x*y
#     return output

# O = mutiply(2 ,4)
# print(O)

# def name(myName , status):
#     print("My name is : " + myName + " \nHe is " + status)

# name("Pushp", "Student")    
#NESTED FUNCTIONS
def f(x):
   x = x + 1
   print('in f(x): x =', x)
   return x

x = 3
z = f(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)

def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)
    x = x + 1
    print('in g(x): x = ', x)
    h(x)
    return x

x = 3
z = g(x)
print('in main program scope: x = ', x)
print('in main program scope: z = ', z)