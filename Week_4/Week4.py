# Week 4 Lab

# 1. Manually arrange the sequence [2 7 9 4 1 5 3 6 0 8] in ascending order using insertion sort, bubble sort and selection sort, showing at each step the new configuration of the sequence.

def insertionSort(l):
    for i in range(1, len(l)):
        currentValue = l[i]
        print(l)
        while i > 0 and l[i - 1] > currentValue:
            l[i] = l[i - 1]
            i = i - 1

        l[i] = currentValue


# l = [2, 7, 9, 4, 1, 5, 3, 6, 0, 8]
# insertionSort(l)
# print(l)


def bubbleSort(l):
    for passNumber in range(len(l) - 1, 0, -1):
        for i in range(passNumber):
            print(l)
            if l[i] > l[i + 1]:
                var = l[i]
                l[i] = l[i + 1]
                l[i + 1] = var


# l = [2, 7, 9, 4, 1, 5, 3, 6, 0, 8]
# bubbleSort(l)
# print(l)


def selectionSort(l):
    for i in range(len(l) - 1, 0, -1):
        maxIndex = 0
        for currentLocation in range(1, i + 1):
            print(l)
            if l[currentLocation] > l[maxIndex]:
                maxIndex = currentLocation

        var = l[i]
        l[i] = l[maxIndex]
        l[maxIndex] = var


# l = [2, 7, 9, 4, 1, 5, 3, 6, 0, 8]
# selectionSort(l)
# print(l)

def guessingGame():
    import random as random
    binary = False                    
    lowNumber, highNumber = 1, 20000

    number = random.randint(lowNumber, highNumber)
    print("A number has been selected from", lowNumber, "and", highNumber)

    lo = 1
    hi = highNumber
    guesses = 0

    for i in range(lowNumber, highNumber):
        #guess = int(input("What is your guess: "))
        if binary:
            guess = lo + (hi - lo) // 2     # integer division
        else:
            guess = random.randint(lo, hi)
        print("Guess:", guess)
        guesses += 1                      
        
        #check the guessed number
        if guess > number:
            print("Lower:")
            hi = guess                        # bring down the upper bound
        elif guess < number:
            print("Higher:")
            lo = guess                        # push up the lower bound
        else:
            break

    print("That took", guesses, "guesses")
    print("That took {0} guesses".format(guesses))

guessingGame()
