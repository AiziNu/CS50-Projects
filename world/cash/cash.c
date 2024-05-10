#include <cs50.h>
#include <stdio.h>

int main(void) {
    int change;

    // Prompt the user for the amount of change owed
    do {
        change = get_int("Change owed: ");
    } while (change < 0);

    // Define the coin values
    int coins[] = {25, 10, 5, 1};
    int num_coins = 0;

    // Calculate the minimum number of coins
    for (int i = 0; i < 4; i++) {
        num_coins += change / coins[i];
        change %= coins[i];
    }

    printf("%d\n", num_coins);

}
