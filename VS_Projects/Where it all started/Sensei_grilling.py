

from BA_Students import Sensei_Standards
import BA_Student_Data

question_prompt = [
    f"Do you love your student, sensei?\nyes\nno\n\n",
]

questions = [
    Sensei_Standards(question_prompt[0], BA_Student_Data.Fuuka.would),
    Sensei_Standards(question_prompt[0], BA_Student_Data.Ichika.would)
]

def ask_sensei():
    for question in questions:
        answer = input(question.ask)
        if answer == question.would:
            print("So you do, sensei, luckily there aren't any laws against students having a relationship with a teacher in Kivotos")
        else:
            print("So you lie sensei, no point on lying.")

ask_sensei()

