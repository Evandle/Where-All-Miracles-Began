
#include <stdio.h>
#include <ctype.h>

int main(void) 
{
    char str[100];
    printf("Give me words: ");
    scanf("%[^\n]", str); 
    printf("You said %s which is pretty %s cool", str, str);
    return 0;
}
