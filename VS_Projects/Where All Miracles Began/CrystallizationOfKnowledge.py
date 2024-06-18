
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
use_resize = get_user_input("Use image up size by multiple?: ", ["yes", "no"])

import contextlib
from PIL import Image

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
        filtered_list = []
        for item in ppsize:
            with contextlib.suppress(ValueError):
                filtered_list.append(int(item))
        if filtered_list: 
            filtered_list.sort()
            return max(filtered_list)
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
            owotranslate += "W" if letter.isupper() else "w"
        else:
            owotranslate += letter
    return owotranslate

if owogo:
    print(owotranslate(input("Your phrase: ")))

def get_grades(quarter_name):
    while True:
        grades = input(f"Enter your grades for {quarter_name}: ").split()
        try:
            return [float(grade) for grade in grades]  # Convert to floats
        except ValueError:
            print("Invalid input. Please enter only numbers separated by spaces.")

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else None

def gradecalmain():
    first_quarter = get_grades("First Quarter")
    second_quarter = get_grades("Second Quarter")
    third_quarter = get_grades("Third Quarter")
    fourth_quarter = get_grades("Fourth Quarter")
    if any(grade_list is None for grade_list in [first_quarter, second_quarter, third_quarter, fourth_quarter]):
        print("You haven't entered grades for all quarters. Calculations cannot proceed.")
        return
    semester_1_average = calculate_average(first_quarter + second_quarter)
    semester_2_average = calculate_average(third_quarter + fourth_quarter)
    final_average = calculate_average(first_quarter + second_quarter + third_quarter + fourth_quarter)
    print(f"Your Semester 1 Average: {semester_1_average:.2f}")  # Format to 2 decimal places
    print(f"Your Semester 2 Average: {semester_2_average:.2f}")
    print(f"Your Final General Average: {final_average:.2f}")

if gradecal:
    gradecalmain()

def Resize_input():
    while True:
        try:
            return int(input("Your size multiplied: "))
        except ValueError:
            print("Invalid input. Please enter only a number.")

def Resize_main():
    n = Resize_input()
    infile = input("Name of file you want to resize: ")
    outfile = input("Name of new resized file: ")
    inimage = Image.open(infile)
    width, height = inimage.size
    outimage = inimage.resize((width * n, height * n)) # type: ignore
    outimage.save(outfile)

if use_resize:
    Resize_main()
