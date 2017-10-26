# Week 3 Lab

# 1. Write a program that reads n words from the standard input, separated by spaces and prints them mirrored (the mirroring function should be implemented recursively). What is the time complexity of the algorithm? Use the BigO notation to express it.

def reverseString(string):
    if len(string) == 0:
        return string
    else:
        return reverseString(string[1:]) + string[0]

def reverseOrder():
    var = reverseString(a)
    stringList = []
    var = var.split()
    for i in var:
        stringList.append(i)
        stringList.reverse()
        newString = " ".join(map(str, stringList))
    return newString

a = input("Please enter a string you want to mirror: ")
print(reverseOrder())
