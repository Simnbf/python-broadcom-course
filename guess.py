import random

def initGame():
    print('Guessing game starting!')
    print('Generating random number between 0 and 100...')
    hiddenNumber = random.randrange(0,10)
    print('Provide your guess, or use the below commands:')
    print("      'stop' - end the game")
    print("      'list' - display current scoreboard")
    attemptCounter = 0
    return hiddenNumber

def saveScore(rn, g):
    scoreGuess.append(g)
    scoreRN.append(rn)

def displayScore():
    print('Score Board:')
    print('Random Number        # Guesses')
    for x in range(len(scoreRN)):
        print(scoreRN[x], '                  ', scoreGuess[x])

scoreGuess = []
scoreRN = []
attemptCounter = 0
hiddenNumber = initGame()

while True:    
    guess  = input()
    match guess.lower():
        case 'list': 
            displayScore()
        case 'stop': 
            print('Guessing game ending...')
            break
        case _:
            if guess.isnumeric():
                if int(guess) > hiddenNumber:
                    attemptCounter+=1                                
                    print('Your guess is  higher!')
                if int(guess) < hiddenNumber:
                    attemptCounter+=1                    
                    print('Your guess is lower!')
                if int(guess) == hiddenNumber:
                    attemptCounter+=1                                
                    print('Bingo! Hidden number is', hiddenNumber)
                    print('It took you', attemptCounter, 'guesses!')
                    saveScore(hiddenNumber, attemptCounter)
                    print('Would you like to play again?')
                    answer = input()
                    if answer.lower() == 'yes':
                        attemptCounter = 0
                        hiddenNumber = initGame()
                    else: 
                        displayScore()
                        print('Game over!')
                        break
            else: print('Please provide a number or command')