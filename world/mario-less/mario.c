#include <cs50.h>
#include <stdio.h>

int main(void) {
    int height;

    // Prompt the user for the height
    do {
        height = get_int("Height: ");
    } while (height <= 0);

    // Draw the pyramid
    for (int i = 0; i < height; i++) {
        // Print the spaces
        for (int j = 0; j < height - i - 1; j++) {
            printf(" ");
        }

        // Print the hashes
        for (int k = 0; k <= i; k++) {
            printf("#");
        }

        printf("\n");
    }

    return 0;
}
