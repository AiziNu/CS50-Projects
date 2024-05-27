#include <stdio.h>

int main(void)
{
    // Prompt the user for their name
    string name = get_string("What is your name?\n");

    // Print a greeting to the user
    printf("hello, %s\n", name);

    return 0;
}
