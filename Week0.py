# Week 0 Lab

import time

# 1. Write a function that deletes a substring from a given character string, specifying the beginning position and the length of the substring.
# removeChar


def removeChar():
    theString = input("Enter String: ")
    print(theString)
    inputDel = input("Enter character to remove: ")
    newStr = theString.replace(inputDel, "")

    print("You have removed", inputDel, "from", theString, ",")
    print("Your new string is", newStr)
    if len(newStr) == 0:
        print("All characters have been removed from the string")
    else:
        strLength = (len(newStr))
        print("The length of your new string is:")
        print(strLength)

# 2. Read from the keyboard a list of positive integers, for example: 1, 4, 7, 9
# a. Write a function that prints the binary representation of the numbers in the list, for the example above it is: 1: 0001 4: 0100 7: 0111 9: 1001


def binaryRep():
    inputString = (input("Enter a list of positive integers: "))
    firstList = list(inputString)
    print("You have entered: ", firstList)
    newList = []

    for char in firstList:
        if char.isdigit():
            if int(char) > 0:
                newList.append(char)
            else:
                pass

    print("If you have entered alphanumeric characters, we have removed it from your list."), time.sleep(1)
    newList = list(map(int, newList))
    print("Your new list is: ", newList), time.sleep(1)
    binaryList = list(map(bin, newList))
    print("Your list in binary is: "), time.sleep(2)
    print(binaryList)

binaryRep()
