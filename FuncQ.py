def my_function(name , age):
    print("My name is " + name + " and my age is " + str(age))
my_function("Rishabh", 18)    

def employe(name , salary = (10000)):
    print(name + "(" + str(salary) + ")")
employe("Ben" , 120000 )    
employe("Bob")
employe("Mike" , 15000)

def details(name ,**data):
    print(name)
    for i ,j in data.items():
        print(i,j)
details("Rishabh" ,place="M.P" , age = 18)
