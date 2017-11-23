# Week 0 Lab

# 1. Write a function that deletes a substring from a given character string, specifying the beginning position and the length of the substring.
import unittest

def removeChar():
    theString = input("Enter String: ")
    print(theString)
    inputDel = input("Enter character to remove: ")
    newStr = theString.replace(inputDel, "")

    print("You have removed", inputDel, "from", theString, ",")
    print("Your new string is: ")
    print(newStr)
    if len(newStr) == 0:
        print("All characters have been removed from the string")
    else:
        strLength = (len(newStr))
        print("The length of your new string is:")
        print(strLength)

removeChar()
# 2. Read from the keyboard a list of positive integers, for example: 1, 4, 7, 9


def ReadKeyboard():
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

    print("If you have entered alphanumeric characters, we have removed it from your list.")
    newList = list(map(int, newList))
    print("Your new list is: ", newList)

    # a. Write a function that prints the binary representation of the numbers in the list, for the example above it is: 1: 0001 4: 0100 7: 0111 9: 1001
    def binaryRep():
        intLiteral = list(map(bin, newList))
        global binaryList
        binaryList = []
        for i in intLiteral:
            binaryList.append(i[2:])
        print("Your list in binary is: ")
        print(binaryList)

        # b. Print the numbers from the previous list that are palindromes. For example, 9: 1001 is a palindrome.
        def palindromes():
            reversedBinary = []
            for i in binaryList:
                reversedBinary.append(i[::-1])
                compare = set(binaryList) & set(reversedBinary)
            if bool(compare) == True:
                print("These are the palindromes in this binary list: ")
                compare = list(compare)
                print(compare)
                # c. Remove all the numbers in the list whose binary representation is a palindrome and print the list after their removal.

                def removePalindromes():
                    global binaryList
                    noPalindromes = set(binaryList) - set(compare)
                    print("All palindromes have been removed from the list")
                    print(list(noPalindromes))
                # removePalindromes()
            else:
                print("There is no palindrome in this binary list")
        # palindromes()
    # binaryRep()
# ReadKeyboard()
