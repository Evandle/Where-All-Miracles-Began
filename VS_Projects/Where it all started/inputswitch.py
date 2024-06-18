
def get_user_input(prompt, valid_inputs):
    # sourcery skip: boolean-if-exp-identity, remove-unnecessary-cast
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_inputs:
            return True if user_input == "yes" else False
        else:
            print("Invalid input. Please try again.")

