#include <stdio.h>
#include <ctype.h>
#include <string.h>

char choice1(char* prompt, char* valid_inputs, char* outputA, char* outputB, char* outputC, char* outputD, char* User_Choice){
    char user_input[100];
    printf("%s\n\n: ", prompt);
    fgets(user_input, sizeof(user_input), stdin);
    user_input[strcspn(user_input, "\n")] = '\0';
    if (strchr(valid_inputs, user_input[0]) != NULL) {
        *User_Choice = user_input[0];
        if (user_input[0] == 'a'){
            printf("%s\n", outputA);
        }
        if (user_input[0] == 'b'){
            printf("%s\n", outputB);
        }
        if (user_input[0] == 'c'){
            printf("%s\n", outputC);
        }
        if (user_input[0] == 'd'){
            printf("%s\n", outputD);
        }
        return user_input[0];
    } else {
        printf("Invalid input. Please try again.");
        return '_'; // Return a default value in case of invalid input
    }
}

int main(void){
    char User_Choice = '_';
    char List_Choice[] = {'a', 'b', 'c', 'd'};
    printf("%c", choice1("a : Tell the truth. b : Lie.\nc : Yes. d : Say nothing.", List_Choice, 
    "In my defense Lori asked for it.\n", "Wha... what are you talking about? I have no clue about that.\n", "Yes\n", "...\n", 
    &User_Choice));
    return 0;
}