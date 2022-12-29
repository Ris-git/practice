# def add(x,y,z = 0):
#     return x+y+z

# print(add(3,4))
# print(add(3,4,5))

class Bird:
    def wings(self):
        print("Bird has two wings")
    def eyes(self):
        print("Bird has two eyes")
    def fly(self):
        print("Most of the birds can fly")
class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")

class Ostrich(Bird):
    pass
    # def fly(self):
    #     print("Ostrich cannot fly")

bird = Bird()
sparrow = Sparrow()
ostrich = Ostrich()

bird.eyes()
bird.wings()
bird.fly()
ostrich.fly()

class car:
    pass

class vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.milegae = mileage

class child(vehicle):
    pass
    

obj = child("ABC" , 19)
print(obj.name)


