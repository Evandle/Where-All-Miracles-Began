
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    char FirstName[100];
    char SecondName[100];
    printf("Name\n");
    fgets(FirstName, sizeof(FirstName) - 1, stdin);
    printf("Another Name\n");
    fgets(SecondName, sizeof(SecondName) - 1, stdin);
    FirstName[strcspn(FirstName, "\n")] = '\0';
    SecondName[strcspn(SecondName, "\n")] = '\0';
    if (FirstName == SecondName)
    {
        printf("Different");
    }
    else if (strcmp(FirstName, SecondName) == 0)
    {
        printf("%s are the same", FirstName);
    }
    else
    {
        printf("Error");
    }
    return 0;
}

