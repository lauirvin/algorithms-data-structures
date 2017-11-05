# Week 1 Lab

# 1. Write a method that combines two strings, by taking one character from the first string, then one from the second string and so on. Once one string has no characters left it should carry on with the other string.
import unittest

def mergeStrings(string1, string2):
    string1List = []
    string2List = []

    if len(string1) == 0:
        pass
    else:
        for char in string1:
            string1List.append(char)

    if len(string2) == 0:
        pass
    else:
        for char in string2:
            string2List.append(char)

    mergedStringList = [j for i in zip(string1List, string2List) for j in i]

    mergedString = ''.join(mergedStringList)
    print("Your combined string is: ", mergedString)

#mergeStrings()

# 2. Check if a 3 digit number is an Armstrong number. An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself.

def armstrongNumber():
    number = input("Input a 3 digit number: ")
    numberList = []
    
    if len(number) < 3:
        print("Your number is not a 3 digit number.")
    else:
        for char in number:
            numberList.append(char)
            number = int(number)
            
    firstNumber = int(numberList[0])**3
    secondNumber = int(numberList[1])**3
    thirdNumber = int(numberList[2])**3
    combinedNumbers = firstNumber + secondNumber + thirdNumber
    
    if number == combinedNumbers:
        print("Yes")
    else:
        print("No")
        
            
#armstrongNumber()

class IsAnagramTests(unittest.TestCase):

    def testOne(self):
        self.assertEquals(mergeStrings("diana","anaid"))

def main():
    unittest.main()

if __name__ == '__main__':
    
    main()
