# Week 3 Lab

# 1. Write a program that reads n words from the standard input, separated by spaces and prints them mirrored (the mirroring function should be implemented recursively). What is the time complexity of the algorithm? Use the BigO notation to express it.

import unittest
import string

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

# a = input("Please enter a string you want to mirror: ")
# print(reverseOrder())



# 2. Write a recursive version of linear search on an array of integers. What is the time complexity of the algorithm? Use the BigO notation to express it.

def linearSearch(l, target):
    if len(l) == 0:
        return False
    if l[0] == target:
        return True
    return linearSearch(l[1:], target)


#print(linearSearch([1,3,5,7,9], 21))

class IsAnagramTests(unittest.TestCase):
    def testTwo(self):
        self.assertTrue(reverseString("hello world"))
    def testThree(self):
        self.assertTrue(linearSearch("[1,3,5,7,9]","5"))
    def testFour(self):
        self.assertFalse(linearSearch("[1,3,5,7,9]","21"))

def main():
    unittest.main()

if __name__ == '__main__':
    
    main()

