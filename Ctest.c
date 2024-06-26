
#include <stdio.h>
#include <ctype.h>

#include <stdio.h>
#include <ctype.h>
#include <string.h>

typedef struct
{
    char name[100];
    char school[100];
    char gender[100];
    char gun[100];
}
Student;

int main(void) 
{
    char num[100];
    printf("Give me num: ");
    scanf("%d", num);
    Student waterwater[100];
    waterwater.name = num;
    printf("You said %d which is pretty %d cool", waterwater, waterwater);

    return 0;
}
