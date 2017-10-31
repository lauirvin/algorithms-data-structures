Week 2

1. 

(a) Pseudocode for adding two polynomials:

function polynomials(p1, p2, degree1, degree2):
	output <- empty list
	if degree1 < degree 2:
		insert p2[0] to position [0] in output
		degreeDifference = degree2 - degree1
		output <- output + [ j + i for j, i in zipped(p1, p2[degreeDifference:])]
		finalDegree <- degree2
	else if degree2 < degree1:
		degreeDifference <- degree1 - degree2
		output <- output + [ j + i for j, i in zipped(p1[degreeDifference:], p2)]
		finalDegree <- degree1

return output
return finalDegree

(c) Write the pseudocode for computing the derivative for each of the two polynomials:

function polynomialDerivative (p, degree):
	set derivativeFormula <- nx^(n-1)
		for each number in p:
			p* [i]
	reduce p[i] by 1
	degree <- degree -1

return p
return degree

2. Write the pseudocode and code for a function that determines whether an array is a palindrome

function palindrome(L):
	L <- list
	K <- empty list

	for each number in L:
		reverse(L) and append to K

	if L == K:
		output Yes
	else:
		No
		
	
