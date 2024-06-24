
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

// Temporary functions.
int Morning1();

// Choice maker.
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


// The main function that calls the events and sets the timeline accordingly.
int main(void){
    char Player[100];
    char Maingirl[100];
    printf("What is your name?\n: ");
    fgets(Player, sizeof(Player) - 1, stdin);
    Player[strcspn(Player, "\n")] = '\0';
    printf("Who's the girl you want to settle down with?\n: ");
    fgets(Maingirl, sizeof(Maingirl) - 1, stdin);
    Maingirl[strcspn(Maingirl, "\n")] = '\0';
    Morning1(Player, Maingirl);
    return 0;
}


// Morning, the start of the game's story line.
int Morning1(const char* Player, const char* Maingirl){
    char User_Choice = '_';
    char List_Choice[] = {'a', 'b', 'c', 'd'};
    
    printf("%s let out an exasperated groan while stretching his arms. %s had been hard at work sorting through documents on his computer.\n\n", Player, Player);
    usleep(9000000);
    printf("\"Hey %s! Whatcha up to?\" A voice overflowing with energy and was quite loud was heard from behind %s. He looked behind to see the bright smile of %s.\n\n", Player, Player, Maingirl);
    usleep(9000000);
    printf("\"Just sorting some documents. You don't have anything to do, %s?\" %s was curios on her sudden visit.\n\n", Maingirl, Player);
    usleep(9000000);
    printf("\"Nope, I was kinda just wandering around thinking about what to do, and before I knew it, I'm right outside of your front door so I decided to invite myself in. I'm not bothering you, am I, %s?\" %s was as casual as ever as she explained that she just seemed to find her way here.\n\n", Player, Maingirl);
    usleep(9000000);
    printf("%c", choice1("a : Tell the truth. b : Lie.\nc : Yes. d : Say nothing.", List_Choice, 
    "In my defense Lori asked for it.\n", "Wha... what are you talking about? I have no clue about that.\n", "Yes\n", "...\n", 
    &User_Choice));
    usleep(9000000);
    return 0;
}
