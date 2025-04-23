# Python Wordle Clone
# by Lucas Dias

This project is a simple, text-based clone of Wordle made in Python. 

## How to Play

1.  **Prerequisites:** Make sure you have Python 3 installed.
2.  **Word List:** You need a file named `wordList.txt` in the same directory as `wordle.py`. This file should contain a list of valid 5-letter words, one word per line. The game will randomly select a word from this list and validate guesses against it.
3.  **Gameplay:**
    *   You have 6 attempts to guess the secret 5-letter word.
    *   Enter your 5-letter guess when prompted.
    *   After each guess, feedback will be provided for each letter:
        *   `[X]` : The letter `X` is in the word and in the correct position.
        *   `(X)` : The letter `X` is in the word but in the wrong position.
        *   ` X ` : The letter `X` is not in the word.
    *   Use the feedback to refine your next guess.
    *   The game ends when you guess the word correctly or run out of attempts.

## Files

*   `wordle.py`: The main script with game logic.
*   `wordList.txt`: The text file containing the list of possible 5-letter words.

## Notes

*   Words in `wordList.txt` should be lowercase.
*   The script currently only handles 5-letter words.
*   The game uses simple text markers for feedback instead of colors.
