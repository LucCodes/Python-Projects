# Python Wordle Clone
# by Lucas Dias

This project is a simple, text-based clone of Wordle

## How to Play

1.  **Prerequisites:** Ensure you have Python 3 installed.
2.  **Word List:** You need a file named `wordList.txt` in the same directory as `wordle.py`. This file should contain a list of valid 5-letter words, one word per line. The game will randomly select the secret word from this list and validate guesses against it.
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

*   `wordle.py`: The main Python script with game logic.
*   `wordList.txt`: A text file containing the list of possible 5-letter words (provide or create this).

## Notes

*   Words in `wordList.txt` should be lowercase.
*   The script currently only handles 5-letter words.
*   The game uses simple text markers for feedback instead of colors.
