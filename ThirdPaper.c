#include <stdio.h>
#include <ctype.h>
#include <string.h>

char choice1(char* prompt, char* valid_inputs, char outputA, char outputB, char outputC, char outputD, char* User_Choice){
    char user_input[100];
    
    printf("%s", prompt);
    fgets(user_input, sizeof(user_input) - 1, stdin);
    user_input[strcspn(user_input, "\n")] = '\0';
    while (true){
    if (strcmp(user_input, valid_inputs) == 0){
        if (strcmp(user_input, "a") == 0){
            *User_Choice = 'a';
        }
        else if (strcmp(user_input, "b") == 0){
            return 'b';
        }
        else if (strcmp(user_input, "c") == 0){
            return 'c';
        }
        else if (strcmp(user_input, "d") == 0){
            return 'd';
        }
        else{
            printf("Error");
        }
    }
    else{
        printf("Invalid input. Please try again.");
    }
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