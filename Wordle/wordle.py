import random
from collections import Counter

def main():
    try:
        with open("wordList.txt", 'r') as wordFile:
            wordList = [line.strip().lower() for line in wordFile.readlines() if len(line.strip()) == 5]
        if not wordList:
            print("Error: wordList.txt is empty or contains no 5-letter words.")
            return
    except FileNotFoundError:
        print("Error: wordList.txt not found in the current directory.")
        return

    puzzleSolution = getWord(wordList)
    # print(f"Debug: The word is {puzzleSolution}") # debugging
    playGame(puzzleSolution, wordList)

def getWord(wordList):
    return random.choice(wordList) # 

def evaluate_guess(guess, solution):
    """Evaluates a guess against the solution, returning feedback for each letter.

    Returns:
        list: A list of strings ('correct', 'present', 'absent') for each letter.
    """
    feedback = [''] * 5
    solution_counts = Counter(solution)
    guess_counts = Counter()

    # first pass: mark correct letters
    for i in range(5):
        if guess[i] == solution[i]:
            feedback[i] = 'correct'
            solution_counts[guess[i]] -= 1
            guess_counts[guess[i]] += 1

    # second pass: mark present (but wrong position) and absent letters
    for i in range(5):
        if feedback[i] == '': # only check letters not already marked 'correct'
            if guess[i] in solution_counts and solution_counts[guess[i]] > 0:
                feedback[i] = 'present'
                solution_counts[guess[i]] -= 1
            else:
                feedback[i] = 'absent'
    return feedback

def display_feedback(guess, feedback):
    """Displays the guess with color-coded feedback (using simple text markers)."""
    display_line = []
    for i in range(5):
        if feedback[i] == 'correct':
            # use markers like [ ] for correct, ( ) for present
            display_line.append(f"[{guess[i].upper()}]")
        elif feedback[i] == 'present':
            display_line.append(f"({guess[i].upper()})")
        else:
            display_line.append(f" {guess[i].upper()} ")
    print(" ".join(display_line))


def playGame(puzzleSolution, wordList):
    # puzzle = ["_", "_", "_", "_", "_"]
    guessLimit = 6
    currentGuessCount = 0
    # lettersInWord = "" 
    solved = False
    guesses_history = [] # Store past guesses and feedback

    print("Welcome to Wordle!")
    print(f"You have {guessLimit} tries to guess the 5-letter word.")
    print("Feedback: [X] = Correct, (X) = Present but wrong spot, X = Absent")

    while currentGuessCount < guessLimit and not solved:
        print(f"\n--- Guess {currentGuessCount + 1} of {guessLimit} ---")

        # Display previous guesses
        for g, f in guesses_history:
            display_feedback(g, f)

        prompt_text = "Guess a 5-letter word: "
        guess = ""
        while True:
            guess = input(prompt_text).lower()

            if len(guess) != 5:
                print("Invalid input: Guess must be 5 letters long.")
                prompt_text = "Please re-enter (5 letters): "
            elif guess not in wordList:
                print("Invalid input: Word not in dictionary.")
                prompt_text = "Please re-enter (valid word): "
            else:
                break # valid guess

        currentGuessCount += 1
        feedback = evaluate_guess(guess, puzzleSolution)
        guesses_history.append((guess, feedback))

        # clear screen or add spacing before showing current guess feedback
        # print("\n" * 2) # optional: add spacing
        print("\nYour guess feedback:")
        display_feedback(guess, feedback)

        if guess == puzzleSolution:
            solved = True
            print(f"\nCongrats! You guessed the word '{puzzleSolution.upper()}' in {currentGuessCount} tries!")
            break

    if not solved:
        print(f"\nSorry, you ran out of guesses. Idiot. The word was '{puzzleSolution.upper()}'.")

main()
