
# Imports.
from tkinter import simpledialog
from time import sleep
import BA_Student_Data
import random
import pyttsx3

# Text to speech Calibration
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# The function that will print and turn the text into speech
def T2S(text):
    print(f"{text}")
    engine.say(f"{text}")
    engine.runAndWait()
    input("")
    
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
    while True:
        pick = simpledialog.askstring("Who's the lone you truly love?", f"Who's the girl you wish to settle down with?: \n{names_list}")
        if pick in students:
            for girl in students:
                if pick in girl:
                    return students[girl]
        else:
            print("Invalid input, please try again.")

# Ask sensei's name.
player = simpledialog.askstring("What's your name sensei?", "Your name:") + "-sensei"
T2S(f"Welcome to the epilogue of the story of our youth, {player}. Remember, click the terminal and press enter to continue.")

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

# A conversation about sensei's encounter with an interesting student. Part of the choices in Conversation 1.
def conversation1_A():
    T2S(
        f"{maingirl} looked at {player} curiously \"Oh? is that so, so what happened?\"\n"
    )
    T2S(
        f"\"I met an interesting Trinity student named Natsu, she went all the way to SCHALE in order to find some promotional cake pops. Unfortunately for her SCHALE's Angel 24 branch was never stocked with the item to begin with.\"\n"
    )
    T2S(
        f"{maingirl} chuckled in amusement, \"Ah she must have been quite the enthusiast. But I dont see how tiring she can be, unless you help her to find the elusive cake pops all around the city? I know you like helping your students, but that's kinda much, my dear.\"\n"
    )
    T2S(
        f"{player} scratched the back of his head as he denied, \"Nah I didn't, the tiring part was listening to her as she spoke poetically like she was writing an essay, with all the elegant tones and verbose words, heck she even pulled out some alliterations.\"\n"
    )
    T2S(
        f"He had a thoughtful expression as if thinking of something fond, \"Especially when she started talking about sweets, she was very passionate about it. it was honestly quite charming, but it kinda got tiring when she started talking about how Kivotos would implode without sweets, how sweets is one of the top three commodities in Kivotos, then she started went all philosophical about sweets.\"\n"
    )
    T2S(
        f"{maingirl} grimaced from the thought, \"Yaiks, that does sound mentally draining.\" she patted {player} on the back \"Students will be students, with there own little unique quirks. You just gotta be patient with them.\"\n"
    )
    T2S(
        f"{player} smiled at his wife's care, \"Dont worry about it, as a teacher and an adult I totally understand what your saying honey. But you know that wasn't even the end yet, seeing that she likes sweets I gave her some left over sweets from my homeland.\"\n"
    )
    T2S(
        f"{maingirl} smirked, \"Let me guess, she started going all philosophical and seeing that you gave her sweets, maybe even connect it to romance.\"n"
    )
    T2S(
        f"{player} was certainly impressed by his wife's deductive capabilities, \"Yup, pretty much, she associated the sharing of sweets to the sharing of happiness. Because the sweets was from my homeland and thus rare, she said that it is akin to shaking a part of my self.\"\n"
    )
    T2S(
        f"\"Huh, what an interesting girl. Quite charming indeed.\" {maingirl} nodded in understanding while chuckling abit.\n"
    )
    sleep(1)

# Sensei asking about wifey's day and her teasing him, and a bit of an interrogation. Part of the choices in Conversation 1.
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
    T2S(5)
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
    T2S(
        f"\"Yea, thank you dear, you really are the best.\" {player} gave {maingirl} a bright smile in relief.\n"
    )
    sleep(1)
# A conversation about a random student. Part of the choices in Conversation 1.
def conversation1_C():
    
    RandomStudent = Random_Student_Data # Transfer to a place holder for convenience.
    
    T2S(
        f"\"{RandomStudent}? What's about her?\" "
    )
    
    

# Sensei telling wifey on how much he loves and appreciated her. Part of the choices in Conversation 1.
def conversation1_D():
    T2S(
        f"{maingirl} blushed"
    )
    
    
    

# The evening conversation, the first in the timeline
def evening_1():
    T2S(
        f"\n{player} was tired due to the day's work, he went home sleepy and low on energy. Knocking on his home's door, he heard \"I'm coming honey.\" and after a couple seconds it opened revealing {maingirlfull} greeting him with a wide smile on her face.\n"
    )
    T2S(
        f"\"Welcome home {player}\" her smile was so bright and loving that it healed his tired mind and heart. \"I'm home my dear {maingirl}.\"\n"
    )
    choice1(f"a : Hug {maingirl}. b : Head pat {maingirl}.\nc : Kiss {maingirl} on the lips. d : Kiss {maingirl} on the forehead.", ["a", "b", "c", "d"],
        f"{player} gave {maingirl} a firm hug.", f"{player} smiled and patted {maingirl} on the head.", f"{player} gave {maingirl} a nice quick kiss on the lips.", f"{player} gave {maingirl} a quick kiss on the forehead.",
        3, 1, 2, 1)
    
    T2S(
        f"\n{player}'s action set her heart alight with warmth and love.\n\n{maingirl} smiled brightly, \"Good evening, honey, dinner will be ready soon.\"\n"
    )
    T2S(
        f"{player}'s lips couldn't help but tick at the corners. He entered the living room and pulled out a chair for him to sit on. He sat down and watched as his beloved prepared two plates of food and set it in front of him and across him. It smelled delicious. \"Thank you dear.\"\n"
    )
    T2S(
        f"The couple began eating while {player} sipped his coffee and read the Canny News newspaper next to {maingirl}. {maingirl} couldn't help but giggle, it was just like in the movies and felt very domestic, she enjoyed every second of it. She loved this kind of life, spending every day with the one she loved and sharing all of life's little moments together.\n"
    )
    T2S(
        f"They ate quietly until {maingirl} finished her plate and they cleaned up together. He thought about what he should talk about with {maingirl}.\n"
    )
    sleep(1)

# The main function, it manages the flow of the story's timeline and paths.
def main():
    evening_1()
    conversation1 = choice1(f"a : Talk about how the day went for you. b : Ask how her day went.\nc : Talk about another student. d : Talk about how much you appreciate her.", ["a", "b", "c", "d"],
        f"\"I had a particularly interesting day today, an interesting but tiring one.\"\n", "How did your day went dear?", f"\"Remember {PullOneTimes()}?\"", f"I'm really lucky to have you {maingirl}",
        1, 1, 0, 3)
    
    if conversation1 == "a":
        conversation1_A()
        Affection_level + 1 # type: ignore
    elif conversation1 == "b":
        conversation1_B()
        Affection_level + 2 # type: ignore
    elif conversation1_C == "c":
        conversation1_C()
        Affection_level + 2 # type: ignore
    elif conversation1 == "d":
        conversation1_D()
        Affection_level + 4 # type: ignore
    
    
    

# The main thingy. Calls main function.
if __name__ == '__main__':
    main()

