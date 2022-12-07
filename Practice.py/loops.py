import random
def get_choices():
    my_choice = input("Enter a choice(rock, paper , scissors : ")
    choice = ["rock , paper, scissors"]
    computer_choice = random.choices(choice)
    
    while my_choice!= computer_choice:
        return my_choice


s = get_choices()
print(s)
    

            

