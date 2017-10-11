# Week 1 Lab

# 1. Write a method that combines two strings, by taking one character from the first string, then one from the second string and so on. Once one string has no characters left it should carry on with the other string.

def mergeStrings():
    string1 = input("Please enter String 1: ")
    string2 = input("Please enter string 2: ")
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

mergeStrings()
