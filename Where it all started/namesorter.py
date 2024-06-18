names = input("Names of your waifus: ").split()
print(names)

def greet(one, two, three, four):
    print(
        f"Congratulation {one} you are sensei's favorite student and even desired wife!"
    )
    print(
        f"Congratulation {two} you are sensei's second favorite student and even his best waifu!"
    )
    print(
        f"Congratulation {three} you are sensei's third favorite student, better than most students."
    )
    print(
        f"Congratulation {four} you are sensei's fourth favorite student, better than most students."
    )

greet(names[0], names[1], names[2], names[3])
