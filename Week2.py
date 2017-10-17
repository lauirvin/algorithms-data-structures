#Week 2 Lab

#1. Read the degree of two polynomials and their coefficients, all integers, from the standard input.

p1 = [3,1,9]
p2 = [2,1,2,1]
degree1 = 2
degree2 = 3
finalDegree = 0

if degree1 < degree2:
    finalDegree = degree2 - degree1
elif degree2 < degree1:
    finalDegree = degree1 - degree2

output = [j + i for j,i in zip(p1[,p2)]

print(output)