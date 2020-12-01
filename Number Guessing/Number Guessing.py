import random

guessedNumbers = []
didUserGuess = False

print("Welcome to Number Guessing!")
print("Enter the Minimum and Maximum Numbers.")

while not didUserGuess:
    didUserInputRange = False

    while not didUserInputRange:
        minRange = input("Enter Minimum Number: ")
        maxRange = input("Enter Maximum Number: ")

        if (minRange.isnumeric() and maxRange.isnumeric() and minRange and maxRange):
            if minRange == maxRange:
                rangeMin = None
                rangeMax = None
                print('Minimum Number is equal to Maximum Number')
            elif minRange > maxRange:
                print('Minimum Number is greater than Maximum Number')
            else:
                didUserInputRange = True
                break

    minRange = int(minRange)
    maxRange = int(maxRange)
    amtOfTries = 0
    randomNumber = random.randint(minRange, maxRange)

    maxTries = input("Enter Maximum of Tries before forfit: ")
    didUserGuessRight = False

    if (maxTries.isnumeric() is False):
        print("Maximum number of tries set as default value, 10")
        maxTries = 10
    else:
        print("Maximum number of tries set as, " + maxTries)

    print("Guess a number from " + str(minRange) + " to " + str(maxRange))

    while not didUserGuessRight:
        if (int(amtOfTries) == int(maxTries)):
            print("Maximum number of tries!")
            break
        else:
            amtOfTries += 1
            userGuess = int(input("Guess: "))

            if userGuess:
                if (userGuess == randomNumber):
                    print("You got it!")
                    didUserGuessRight = True
                    break
                elif (userGuess > maxRange):
                    print("Guess is higher than Maximum Range set! Please try again.")
                    didUserGuessRight = False
                elif (userGuess < minRange):
                    print("Guess is lower than Minimum Range set! Please try again.")
                    didUserGuessRight = False
                else:
                    print("Nope! Thats not correct. Try again.")
                    didUserGuessRight = False