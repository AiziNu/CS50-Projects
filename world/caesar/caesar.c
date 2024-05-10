#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// Function to encrypt a plaintext message using Caesar cipher
string caesar_cipher(string plaintext, int key)
{
    string ciphertext = plaintext;

    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        if (isalpha(plaintext[i]))
        {
            char base = isupper(plaintext[i]) ? 'A' : 'a';
            ciphertext[i] = (plaintext[i] - base + key) % 26 + base;
        }
    }

    return ciphertext;
}

int main(int argc, string argv[])
{
    // Check if the user provided the correct number of command-line arguments
    if (argc != 2)
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }

    // Convert the key from string to integer
    int key = atoi(argv[1]);

    // Get the plaintext message from the user
    string plaintext = get_string("plaintext: ");

    // Encrypt the plaintext message using Caesar cipher
    string ciphertext = caesar_cipher(plaintext, key);

    // Output the ciphertext message
    printf("ciphertext: %s\n", ciphertext);

    return 0;
}
