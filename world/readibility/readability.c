#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

// Function to count letters in a string
int count_letters(string text)
{
    int count = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            count++;
        }
    }
    return count;
}

// Function to count words in a string
int count_words(string text)
{
    int count = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isspace(text[i]) || i == n - 1)
        {
            count++;
        }
    }
    return count;
}

// Function to count sentences in a string
int count_sentences(string text)
{
    int count = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count++;
        }
    }
    return count;
}

// Function to calculate the Coleman-Liau index
int calculate_index(int letters, int words, int sentences)
{
    float L = ((float)letters / words) * 100;
    float S = ((float)sentences / words) * 100;
    return (int)(0.0588 * L - 0.296 * S - 15.8 + 0.5);
}

// Function to print the grade level
void print_grade(int index)
{
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", index);
    }
}

int main(void)
{
    // Get input text from the user
    string text = get_string("Text: ");

    // Count letters, words, and sentences
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Calculate the Coleman-Liau index
    int index = calculate_index(letters, words, sentences);

    // Print the grade levelwo 
    print_grade(index);

    return 0;
}
