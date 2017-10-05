# Week 0 Lab

# removeChar


def removeChar():
    theString = input("Enter String: ")
    print(theString)
    inputDel = input("Enter character to remove: ")
    newStr = theString.replace(inputDel, "")
    if len(newStr) == 0:
        print("All characters have been removed from the string")
    else:
        strLength = (len(newStr))
        print("The length of your string is:")
        print(strLength)

def binaryRep():
    inputString = (input("Enter String: "))
    firstList = list(inputString)
    print(firstList)
    newList = []
    for char in firstList:
        if char.isdigit():
            if int(char) > 0:
                newList.append(char)
            else:
                pass

    print(newList)

removeChar()
