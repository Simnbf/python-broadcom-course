import random

def genNumber(a):
    return random.randrange(0,int(a))

def displayScore(a,b,c):
    print('Score Board:')
    print('Game Size       Random Number        # Guesses')
    for x in range(len(a)):
        print(a[x], '            ',b[x], '                  ', c[x])


scoreGuess = []
scoreRN = []
scoreSize = []
attemptCounter = 0

while True:
    print('Guessing game starting!')
    print('Enter game size')
    highNum = input()
    if highNum.isnumeric():
        print('Generating random number between 0 and', int(highNum), '...')
        hiddenNumber = genNumber(highNum)
        print('Provide your guess, or use the below commands:')
        print("      'stop' - end the game")
        print("      'list' - display current scoreboard")
    else:
        print("Invalid number - game ending!")
        break
    

    while True:    
        guess  = input()
        match guess.lower():
            case 'list': 
                displayScore(scoreSize, scoreRN, scoreGuess)
            case 'stop': 
                displayScore(scoreSize, scoreRN, scoreGuess)
                print('Guessing game ending...')
                break
            case _:
                if guess.isnumeric():
                    if int(guess) > hiddenNumber:
                        attemptCounter+=1                                
                        print('Your guess is higher!')
                    if int(guess) < hiddenNumber:
                        attemptCounter+=1                    
                        print('Your guess is lower!')
                    if int(guess) == hiddenNumber:
                        attemptCounter+=1                                
                        print('Bingo! Hidden number is', hiddenNumber)
                        print('It took you', attemptCounter, 'guesses!')   
                        scoreSize.append(highNum)                 
                        scoreGuess.append(attemptCounter)
                        scoreRN.append(hiddenNumber)  # ...
                        print('Would you like to play again?')
                        answer = input()
                        if answer.lower() == 'yes':
                            attemptCounter = 0
                            break
                        else: 
                            displayScore(scoreSize, scoreRN, scoreGuess)
                            print('Game over!')
                            exit()
                else: print('Please provide a number or command')