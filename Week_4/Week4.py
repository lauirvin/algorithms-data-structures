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
