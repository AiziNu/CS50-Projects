#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void encrypt(char *text, int key);

int main(int argc, char *argv[])
{
    if (argc != 2 || atoi(argv[1]) < 1)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int key = atoi(argv[1]) % 26;
    char text[1000];

    printf("plaintext: ");
    fgets(text, sizeof(text), stdin);

    printf("ciphertext: ");
    encrypt(text, key);

    return 0;
}

void encrypt(char *text, int key)
{
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isalpha(text[i]))
        {
            char base = isupper(text[i]) ? 'A' : 'a';
            printf("%c", (text[i] - base + key) % 26 + base);
        }
        else
        {
            printf("%c", text[i]);
        }
    }
    printf("\n");
}
