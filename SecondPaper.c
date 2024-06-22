#include <stdio.h>
#include <ctype.h>
#include <string.h>

int isSubstring(const char* str1, const char* str2) {
    int len1 = strlen(str1);
    int len2 = strlen(str2);

    if (len2 > len1) {
        return 0;
    }

    for (int i = 0; i <= len1 - len2; i++) {
        int j;
        for (j = 0; j < len2; j++) {
            if (str1[i + j] != str2[j]) {
                break;
            }
        }
        if (j == len2) {
            return 1;
        }
    }
    return 0;
}

int main(void) {
    char FirstName[100];
    char SecondName[100];
    fgets(FirstName, sizeof(FirstName), stdin);
    fgets(SecondName, sizeof(SecondName), stdin);
    if (strcmp(FirstName, SecondName) == 0) {
        printf("%s", FirstName);
    } else if (isSubstring(FirstName, SecondName)) {
        printf("different name");
    } else {
        printf("Error");
    }
    return 0;
}