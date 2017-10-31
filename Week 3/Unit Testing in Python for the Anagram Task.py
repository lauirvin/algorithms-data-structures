import unittest
import string

def isAnagram(s1,s2):
    if len(s1)!= len(s2):
        return False
    alphabet = [0]* 26
    for i in s1:
        n = string.ascii_lowercase.index(i)
        alphabet[n] = alphabet[n]+1
    for i in s2:
        n = string.ascii_lowercase.index(i)
        alphabet[n] = alphabet[n]- 1
    for k in alphabet:
        if k != 0:
            return False
    return True


class IsAnagramTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(isAnagram("diana","anaid"))

    def testTwo(self):
        self.assertFalse(isAnagram("diana","ahjsd"))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
