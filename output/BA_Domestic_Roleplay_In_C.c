
#include <stdio.h>
#include <string.h>

// Temporary functions.
int TextPrint();
int Evening1();

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

//The function that controls the printing of text and ease of adding new functionality in text printing.
int TextPrint(const char* Prompt, const char* Player, const char* Maingirl) {
    printf(Prompt, Player, Maingirl, Player);
    return 0;
}

// Morning, the start of the game's story line.
int Morning1(const char* Player, const char* Maingirl){
    TextPrint("%s arrived home tired and weary. %s greeted %s with a smile.\n", Player, Maingirl);
    
    return 0;
}
