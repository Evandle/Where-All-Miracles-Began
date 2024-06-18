
import contextlib

def cube1():
    while True:  # Ensures loop continues until valid input
        cuberswitch = input("Use exponent converter Yes/No?: ").lower() 
        if cuberswitch in ["yes"]:
            return True
        elif cuberswitch in ["no"]:
            return False
        else:
            print("Invalid input. Please try again. (Yes/No)")

# Call the function and store the result
do = cube1()

def ppms():
    while True:
        ppmeasure = input("Use PP Comparer Yes/No?: ").lower()
        if ppmeasure in ["yes", "Yes"]:
            return True
        elif ppmeasure in ["no", "No"]:
            return False
        else:
            print("Invalid input. Please try again.")

dodong = ppms()

def stn1():
    while True:
        stntrue = input("Use Seconds to Normal Yes/No?: ")
        if stntrue in ["yes", "Yes"]:
            return True
        elif stntrue in ["no", "No"]:
            return False
        else:
            print("Invalid input. Please try again.")

seconds_to_normal = stn1()

def cv1():
    while True:
        ptcv1 = input("Use Yuuka's Prototype Calculator V1 Yes/No?: ")
        if ptcv1 in ["yes", "Yes"]:
            return True
        elif ptcv1 in ["no", "No"]:
            return False
        else:
            print("Invalid input. Please try again.")

pcv1 = cv1()

def favstudentswitch():
    while True:
        favestudent1 = input("Want to guess my favorite Blue Archive student Yes/No?: ")
        if favestudent1 in ["yes", "Yes"]:
            return True
        elif favestudent1 in ["no", "No"]:
            return False
        else:
            print("Invalid input. Please try again.")

favswitch = favstudentswitch()

def owotransswitch():
    while True:
        owoswitch = input("Use OwO translator Yes/No?: ")
        if owoswitch in ["yes", "Yes"]:
            return True
        elif owoswitch in ["no", "No"]:
            return False
        else:
            print("Invalid input. Please try again.")

owogo = owotransswitch()

def take():
    return input("Your number: ")

def expof():
    return input("Your exponent number: ")

def cube(base_num, expo1):
    result1 = 1
    for _ in range(expo1):
        result1 = result1 * base_num
    return result1

if do:
    numexpo = int(take())
    numexpo1 = int(expof())
    result = cube(numexpo, numexpo1)
    print(result)

def big_d():
    
    while True:
        ppsize = input("The numbers you want to compare: ").split()
        filtered_list = []  # Empty list to store converted integers
        for item in ppsize:
            with contextlib.suppress(ValueError):
                filtered_list.append(int(item))
        if filtered_list:  # Check if any valid integers were found
            filtered_list.sort()
            return filtered_list[-1]
        else:
            print("No valid numbers entered. Please try again.")

if dodong:
    thebigboi = big_d()
    thebiggis = f"{thebigboi} inch dong"
    print(
        f"{thebiggis} is the biggest PP of them all!"
    )

if seconds_to_normal:
    seconds = int(input("Your time in seconds: "))
    secondstrue = seconds % 60
    minutes = seconds / 60
    minutestrue = int(minutes) % 60
    hours = int(minutes) / 60
    print(
        f"{hours} hours, {minutestrue} minutes, {secondstrue} seconds."
    )

def ypc():
    cal1 = float(input("Your Number: "))
    op1 = input("Your Operator: ")
    cal2 = float(input("Your Number: "))
    
    if op1 == "+":
        return cal1 + cal2
    elif op1 == "-":
        return cal1 - cal2
    elif op1 == "*":
        return cal1 * cal2
    elif op1 == "/":
        return cal1 / cal2
    else:
        return print("Error")

if pcv1:
    finalans = ypc()
    print(
        f"{finalans}"
        )


def favstudentgateway():
    favstudent = "Fuuka"
    guess_count = 5
    guess_limit = 0
    out_of_tries = False
    guess = ""
    while guess != favstudent and not out_of_tries:
        if guess_count > guess_limit:
            print(f"Number of guesses you have: {guess_count} guesses")
            guess = input("Guess my favorite Blue Archive student: ")
            guess_count -= 1
        else:
            print("Sorry, you failed to identify the obvious best wife in Kivotos.")
            out_of_tries = True
            return False
    return True

if favswitch:
    # sourcery skip: assign-if-exp, introduce-default-else, use-named-expression
    favstudentresults = favstudentgateway()
    if favstudentresults:
        print("You are absolutely right! Fuuka is best wife, she would be the best housewife you can ever dream of.")



def owotranslate(phrase):
    owotranslate = ""
    for letter in phrase:
        if letter.lower() in "lr":
            owotranslate = f"{owotranslate}W" if letter.isupper() else f"{owotranslate}w"
        else:
            owotranslate = owotranslate + letter
    return owotranslate

if owogo:
    print(owotranslate(input("Your phrase: ")))

class Student:
    def __init__ (self, name, age, birthday, school, year, club, gun, description, opinion):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.school = school
        self.year = year
        self.club = club
        self.gun = gun
        self.description = description
        self.opinion = opinion
        self.all = f"\n{name}\n{age}\n{birthday}\n{school}\n{year}\n{club}\n{gun}\n{description}\n{opinion}"


def get_user_input(prompt, valid_inputs):
    # sourcery skip: boolean-if-exp-identity, remove-unnecessary-cast
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_inputs:
            return True if user_input == "yes" else False
        else:
            print("Invalid input. Please try again.")

do = get_user_input("Use exponent converter Yes/No?: ", ["yes", "no"])
dodong = get_user_input("Use PP Comparer Yes/No?: ", ["yes", "no"])
seconds_to_normal = get_user_input("Use Seconds to Normal Yes/No?: ", ["yes", "no"])
pcv1 = get_user_input("Use Yuuka's Prototype Calculator V1 Yes/No?: ", ["yes", "no"])
favswitch = get_user_input("Want to guess my favorite Blue Archive student Yes/No?: ", ["yes", "no"])
owogo = get_user_input("Use OwO translator Yes/No?: ", ["yes", "no"])
gradecal = get_user_input("Calculate your general average?: ", ["yes", "no"])

