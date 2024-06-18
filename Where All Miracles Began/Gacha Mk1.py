
import random

def get_user_input(prompt, valid_inputs):
    # sourcery skip: boolean-if-exp-identity, remove-unnecessary-cast
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_inputs:
            return True if user_input == "yes" else False
        else:
            print("Invalid input. Please try again.")



GachaPool = ["Fuuka", "Hina", "Ichika", "Hoshino", "JSF Mob-chan", "Random Mob-chan"]
Your_students = []

def PullTenTimes():
    return random.choices(GachaPool, weights=(10, 2, 2, 2, 10, 80), k=10)

def listsort(students):
    
    for girl in students:
        if girl in Your_students:
            girl = ""
        else:
            Your_students.append(girl)

if do := get_user_input("Want to pull for students Yes/No?: ", ["yes", "no"]):
    while Pull := get_user_input("Do a 10x pull on gacha?: ", ["yes", "no"]):
        listsort(PullTenTimes())
        print(Your_students)



