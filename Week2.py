# Week 2 Lab

# 1. Read the degree of two polynomials and their coefficients, all integers, from the standard input.

# a) Write the pseudocode for adding two polynomials - Written out in Python for algorithm testing.
def polynomials(p1, p2, degree1, degree2):
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

polynomials([3,1,9], [2,1,2,1], 2, 3)
