#include <cs50.h>
#include <stdio.h>
#include <ctype.h>


int calculate(string word){
    int score = 0;
    int letter_score[26]= {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    for(int i=0; word[i] != '\0'; i++){
        if(isalpha(word[i])){
            score += letter_score[toupper(word[i]) - 'A'];
        }
    }
    return score;
}


int main(void) {
    string word1 = get_string("Player 1: ");

    string word2 = get_string("Player 2: ");

    int score1 = calculate(word1);
    int score2 = calculate(word2);

    if (score1 > score2) {
        printf("Player 1 wins!\n");
    } else if (score1 < score2) {
        printf("Player 2 wins!\n");
    } else {
        printf("Tie!\n");
    }
}
