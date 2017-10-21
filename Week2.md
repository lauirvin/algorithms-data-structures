{\rtf1\ansi\ansicpg1252\cocoartf1561
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\b\fs28 \cf0 Week 2
\fs26 \
\
1. \
\
(a) Pseudocode for adding two polynomials:\

\b0 \
polynomials(p1, p2, degree1, degree2):\
	output <- empty list\
	if degree1 < degree 2:\
		insert p2[0] to position [0] in output\
		degreeDifference = degree2 - degree1\
		output <- output + [ j + i for j, i in zipped(p1, p2[degreeDifference:])]\
		finalDegree <- degree2\
	else if degree2 < degree1:\
		degreeDifference <- degree1 - degree2\
		output <- output + [ j + i for j, i in zipped(p1[degreeDifference:], p2)]\
		finalDegree <- degree1\
\
return output\
return finalDegree\
\

\b (b) Write the pseudocode for computing the derivative for each of the two polynomials:\
\

\b0 polynomialDerivative (p, degree):\
	set derivativeFormula <- nx^(n-1)\
		for each number in p:\
			p* [i]\
	reduce p[i] by 1\
	degree <- degree -1\
\
return p\
return degree\
\
\pard\pardeftab720\sl280\partightenfactor0

\b \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 2. Write the pseudocode for computing the derivative for each of the two polynomials:\
\

\b0 armstrongNumber(L):\
	\
	set left of L as first character\
	set right of L as last character\
		while left < right\
			if left =! right\
				return false\
			increment left\
			decrement right\
		return true\
	
\b \
}