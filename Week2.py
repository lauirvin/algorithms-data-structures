# Week 2 Lab

# 1. Read the degree of two polynomials and their coefficients, all integers, from the standard input.

# a) Write the pseudocode for adding two polynomials - Written out in Python for algorithm testing.


def polynomialAddition(p1, p2, degree1, degree2):
    output = []

    if degree1 < degree2:
        output.insert(0, p2[0])
        degreeDifference = degree2 - degree1
        output = output + [j + i for j, i in zip(p1, p2[degreeDifference:])]
        finalDegree = degree2
    elif degree2 < degree1:
        degreeDifference = degree1 - degree2
        output = output + [j + i for j, i in zip(p1[degreeDifference:], p2)]
        finalDegree = degree1

    print("The Res is: ", output)
    print("The Degree is: ", finalDegree)

#polynomialAddition([3,1,9], [2,1,2,1], 2, 3)

# b) Given the following pseudocode, first understand how it works, then implement the code for multiplying the two polynomials in the programming language of your choice


def polynomialMultiplication(p1, p2, degree1, degree2):

    res = [0] * (degree1 + degree2 + 1)
    print(res)

    for i in range(len(p1)):
        for j in range(len(p2)):
            res[i+j] = res[i+j] + (p1[i] * p2[j])
    
    print(res)


polynomialMultiplication([3, 1, 9], [2, 1, 2, 1], 2, 3)
