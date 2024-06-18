

# Imports.
from tkinter import simpledialog
from time import sleep
import BA_Student_Data
import random
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def T2S(text):
    print(f"{text}")
    engine.say(f"{text}")
    engine.runAndWait()


# The student list for posible wife.
students = {
    "Fuuka" : BA_Student_Data.Fuuka.name,
    "Ichika" : BA_Student_Data.Ichika.name,
    "Hina" : BA_Student_Data.Hina.name,
}

# Relevant data and preparations.
GachaPool = ["Fuuka", "Hina", "Ichika"]
Your_students = []
Random_Student_Data = []
Affection_level = 50

# Picks who the lucky student to be sensei's wifey.
def waifu():
    names_list = list(students)
    for _ in range(3):
        pick = simpledialog.askstring("Who's the lone you truly love?", f"Who's the girl you wish to settle down with?: \n{names_list}")
        if pick in students:
            for girl in students:
                if pick in girl:
                    return students[girl]
        else:
            print("Invalid input, please try again.")

# Ask sensei's name.
player = simpledialog.askstring("What's your name sensei?", "Your name:") + "-sensei"
print(f"Welcome to the epilogue of the story of our youth, {player}.")

# Calls the function to close the fated girl. Also a bit con calibrations.
maingirlfull = waifu()
maingirltemp = maingirlfull.split()
maingirl = maingirltemp[1]
Your_students.append(maingirl)

# The function for random student. it rolls for a random student on the list of students.
def PullOneTimes():  # sourcery skip: inline-immediately-returned-variable
    while True:
        Student = random.choices(GachaPool, weights=(1, 1, 1), k=1)
        for girl in Student:
            if girl not in Your_students:
                Random_Student_Data.append(girl)
                return girl

# The one that manages the player's choice
def choice1(prompt, valid_inputs, outputA, outputB, outputC, outputD, Affection1, Affection2, Affection3, Affection4):
    while True:
        user_input = simpledialog.askstring(
            "What would you do sensei?", f"{prompt}"
        ).lower()
        if user_input in valid_inputs:
            if user_input == "a":
                return choice_calibrator(outputA, Affection1, "a")
            elif user_input == "b":
                return choice_calibrator(outputB, Affection2, "b")
            elif user_input == "c":
                return choice_calibrator(outputC, Affection3, "c")
            elif user_input == "d":
                return choice_calibrator(outputD, Affection4, "d")
            else:
                print("Error")
        else:
            print("Invalid input. Please try again.")

# Does the consequences of the choices we made. Tells what heppened and changes the affection meter.
def choice_calibrator(arg0, arg1, arg2):
    T2S(arg0)
    Affection_level + arg1 # type: ignore
    return arg2

def conversation1_B():  # sourcery skip: extract-duplicate-method, remove-redundant-if
    T2S(
        f"{maingirl} thought about if for a couple seconds before saying, \"I've been thinking about you all day long.\"\n"
    )
    
    T2S(
        f"{player} blushed, \"Honey that's cheating teasing me all of a sudden like that.\"\n"
    )
    
    T2S(
        f"{maingirl} grinned, \"I knew I still got it in me, eheh, I was the one who romanced and made you fall for my charm after all.\" she nodded to her own words while complementing herself.\n"
    )
    
    T2S(
        f"\"Anyway, back to your original question, I've just been cleaning the house and practicing in cooking. And of course all the while thinking about you, I wasn't lying about earlier after all.\" {maingirl} smiled at {player}, seeing him a bit flustered was fun and his smile of love was pleasant to see.\n"
    )
    
    T2S(
        f"{player} went and hugged his silly little wife as she giggled in joy. {maingirl} hugged back pretty tightly that {player} could hardly move. \"Uhh, {maingirl}?\"\n"
    )
    
    T2S(
        f"Now that her pray has been caught, {maingirl} while still sporting the same expression spoke casually.\n"
    )
    
    T2S(
        f"\"Well, I also heard a rumour that in the past {player} licked a student's feet.\"\n"
    )
    counter = choice1(f"a : Tell the truth. b : Lie.\nc : Yes. d : Say nothing.", ["a", "b", "c", "d"],
        "In my defense Lori asked for it.\n", "Wha... what are you talking about? I have no clue about that.\n", "Yes\n", "...\n",
        1, -1, 1, 0)
    counter_All = [counter]
    T2S(
        f"\"Collared a student and took her on a walk on all fours?!?!\"\n"
    )
    counter = choice1(f"a : Tell the truth. b : Lie.\nc : Yes. d : Say nothing.", ["a", "b", "c", "d"],
        "Ako lost a bet.\n", "Never happened.\n", "Yes\n", "...\n",
    1, -1, 1, 0)
    counter_All.append(counter)
    T2S(
        f"\"Sniffed a student?\"\n"
    )
    counter = choice1(f"a : Tell the truth. b : Lie.\nc : Yes. d : Say nothing.", ["a", "b", "c", "d"],
        "Which one? The Hina one?\n", "I dont sniff my students.\n", "Yes\n", "...\n",
    1, -1, 1, 0)
    counter_All.append(counter)
    T2S(
        f"\"Slept with a student?!\"\n"
    )
    counter = choice1(f"a : Tell the truth. b : Lie.\nc : Yes. d : Say nothing.", ["a", "b", "c", "d"],
        "It was all platonic, I literally just slept nothing else.\n", "That's just rumours.\n", "Yes\n", "...\n",
    1, -2, 1, 0)
    counter_All.append(counter)
    T2S(
        f"\"Took a bath with a student?!\"\n"
    )
    counter = choice1(f"a : Tell the truth. b : Lie.\nc : Yes. d : Say nothing.", ["a", "b", "c", "d"],
        "It was a mixed hot springs.\n", "I have no clue about that.\n", "Yes\n", "...\n",
    1, -2, 1, 0)
    counter_All.append(counter)
    T2S(
        f"\"Sniffing a student's panties?!\"\n"
    )
    counter = choice1(f"a : Tell the truth. b : Lie.\nc : Yes. d : Say nothing.", ["a", "b", "c", "d"],
        "That happened when I was in the custody of the Prefect Team.\n", "What? no.\n", "Yes\n", "...\n",
    1, -1, 1, 0)
    counter_All.append(counter)
    T2S(
        f"\"Spent time with a student in their 'secret room'?!\"\n"
    )
    counter = choice1(f"a : Tell the truth. b : Lie.\nc : Yes. d : Say nothing.", ["a", "b", "c", "d"],
        "I was just slacking of with Iroha\n", "What does that even mean.\n", "Yes\n", "...\n",
    1, -1, 1, 0)
    counter_All.append(counter)
    if all(choice in ("a", "c") for choice in counter_All):
        T2S(f"\"So you wont even deny these rumours huh {player}? Well at least you didn't lie to me dear.\" {maingirl} released {player} \"Well aren't you a deviant my dear.\"\n")
    elif any(choice in ("b", "d") for choice in counter_All): 
        T2S(f"\"Well, your not the most honest one ain't ya {player}? Dont be shy with me now dear.\" {maingirl} bopped {player} on the nose.\n")
    else:
        T2S(f"\"You dont have to lie to me now dear, I don't really care if so long as you explain yourself properly and repent.\" {maingirl} flicked {player} on the forehead.\n")
        T2S(f"\"Aw\" {player} rubbed his forehead with a bit of shame.\n")
    T2S(
        f"\"Don't worry dear my love for you won't be overcome by those silly things you did in the past.\" {maingirl} made a cheeky grin, \"You can trust me with that.\"\n"
    )
    sleep(10)
    T2S(
        f"\"Yea, thank you dear, you really are the best.\" {player} gave {maingirl} a bright smile in relief.\n"
    )
    sleep(10)
conversation1_B()