import random

def main():
    wordFile = open("wordList.txt", 'r')
    wordList = [line.strip() for line in wordFile.readlines()]
    wordFile.close()

    puzzleSolution = getWord(wordList)
    playGame(puzzleSolution, wordList)

def getWord(wordList):
    x = int(input("Enter a positive integer: "))
    random.seed(x)
    size = len(wordList)
    index = random.randrange(0, size)
    return wordList[index]

def playGame(puzzleSolution, wordList):
    puzzle = ["_", "_", "_", "_", "_"]
    guessLimit = 6
    currentGuessCount = 0
    lettersInWord = ""
    solved = False
    lost_game = False

    print(f"lettersFound: {lettersInWord}  ")
    print(f"Guesses left:  {guessLimit - currentGuessCount}")
    print(" ".join(puzzle) + "  ")
    print("1 2 3 4 5")

    while currentGuessCount < guessLimit and not solved:
        
        prompt_text = "Guess a 5-letter word: "
        
        while True:
            guess = input(prompt_text).lower()

            if len(guess) == 5 and guess in wordList:
                break
            else:
                print("Must be a word from the dictionary that is 5 letters long.")
                
                if currentGuessCount == guessLimit - 1:
                    print(f"You ran out of guesses (due to invalid input on last try). The word was {puzzleSolution}")
                    lost_game = True
                    break
                else:
                    prompt_text = "Please re-enter: "

        if lost_game:
            break

        currentGuessCount += 1

        puzzle = processGuess(guess, puzzleSolution, puzzle)
        lettersInWord = updateLettersInWord(guess, puzzleSolution, lettersInWord)

        if guess == puzzleSolution:
            solved = True
            remaining_guesses_on_win = guessLimit - currentGuessCount
            print(f"\nCongrats! You won! with {remaining_guesses_on_win} guesses left")
            break

        if currentGuessCount < guessLimit:
            print(f"\nlettersFound: {lettersInWord}  ")
            print(f"Guesses left:  {guessLimit - currentGuessCount}") 
            print(" ".join(puzzle) + "  ")
            print("1 2 3 4 5")
        elif currentGuessCount == guessLimit and not solved:
             print(f"\nYou ran out of guesses. The word was {puzzleSolution}")

def processGuess(guess, puzzleSolution, puzzle):
    puzzleList = puzzle.copy()

    for i in range(5):
        if guess[i] == puzzleSolution[i]:
            puzzleList[i] = guess[i]

    return puzzleList

def updateLettersInWord(guess, puzzleSolution, lettersInWord):
    for i in range(5):
        if guess[i] != puzzleSolution[i] and guess[i] in puzzleSolution and guess[i] not in lettersInWord:
            lettersInWord += guess[i]
    return lettersInWord

main()
