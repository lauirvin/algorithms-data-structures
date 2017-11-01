1. Manually arrange the sequence [2 7 9 4 1 5 3 6 0 8] in ascending order using insertion sort, bubble sort
and selection sort, showing at each step the new configuration of the sequence. How many
comparisons and how many element moves were used by each method? Which is the best performing
method for sorting this array of integers? Which would be the worst arrangement of this sequence?

Insertion Sort:

[2 7 9 4 1 5 3 6 0 8]	Assume 2 is a sorted list of 1 item
[2 7 9 4 1 5 3 6 0 8] 	inserted 7
[2 7 9 4 1 5 3 6 0 8]	inserted 9
[2 4 7 9 1 5 3 6 0 8]	inserted 4 
[1 2 4 7 9 5 3 6 0 8]	inserted 1 
[1 2 4 5 7 9 3 6 0 8]	inserted 5 
[1 2 3 4 5 7 9 6 0 8]	inserted 3
[1 2 3 4 5 6 7 9 0 8]	inserted 6 
[0 1 2 3 4 5 6 7 9 8]	inserted 0 
[0 1 2 3 4 5 6 7 8 9]	inserted 8 

[0 1 2 3 4 5 6 7 8 9]

How many comparisons and how many element moves were used by each method?

7 element moves and 10 comparisons 

Bubble Sort:

First pass:
[2 7 9 4 1 5 3 6 0 8]
[2 7 9 4 1 5 3 6 0 8]
[2 7 9 4 1 5 3 6 0 8]
[2 7 4 9 1 5 3 6 0 8]
[2 7 4 1 9 5 3 6 0 8]
[2 7 4 1 5 9 3 6 0 8]
[2 7 4 1 5 3 9 6 0 8]
[2 7 4 1 5 3 6 9 0 8]
[2 7 4 1 5 3 6 0 9 8]
[2 7 4 1 5 3 6 0 8 9]
Second pass:
[2 7 4 1 5 3 6 0 8 9]
[2 7 4 1 5 3 6 0 8 9]
[2 4 7 1 5 3 6 0 8 9]
[2 4 1 7 5 3 6 0 8 9]
[2 4 1 5 7 3 6 0 8 9]
[2 4 1 5 3 7 6 0 8 9]
[2 4 1 5 3 6 7 0 8 9]
[2 4 1 5 3 6 0 7 8 9]
[2 4 1 5 3 6 0 7 8 9]
[2 4 1 5 3 6 0 7 8 9]
Third pass:
[2 4 1 5 3 6 0 7 8 9]
[2 4 1 5 3 6 0 7 8 9]
[2 1 4 5 3 6 0 7 8 9]
[2 1 4 5 3 6 0 7 8 9]
[2 1 4 3 5 6 0 7 8 9]
[2 1 4 3 5 6 0 7 8 9]
[2 1 4 3 5 0 6 7 8 9]
[2 1 4 3 5 0 6 7 8 9]
[2 1 4 3 5 0 6 7 8 9]
[2 1 4 3 5 0 6 7 8 9]
Fourth pass:
[2 1 4 3 5 0 6 7 8 9]
[1 2 4 3 5 0 6 7 8 9]
[1 2 4 3 5 0 6 7 8 9]
[1 2 3 4 5 0 6 7 8 9]
[1 2 3 4 5 0 6 7 8 9]
[1 2 3 4 0 5 6 7 8 9]
[1 2 3 4 0 5 6 7 8 9]
[1 2 3 4 0 5 6 7 8 9]
[1 2 3 4 0 5 6 7 8 9]
[1 2 3 4 0 5 6 7 8 9]
Fifth pass:
[1 2 3 4 0 5 6 7 8 9]
[1 2 3 4 0 5 6 7 8 9]
[1 2 3 4 0 5 6 7 8 9]
[1 2 3 4 0 5 6 7 8 9]
[1 2 3 0 4 5 6 7 8 9]
[1 2 3 0 4 5 6 7 8 9]
[1 2 3 0 4 5 6 7 8 9]
[1 2 3 0 4 5 6 7 8 9]
[1 2 3 0 4 5 6 7 8 9]
[1 2 3 0 4 5 6 7 8 9]
Sixth pass:
[1 2 3 0 4 5 6 7 8 9]
[1 2 3 0 4 5 6 7 8 9]
[1 2 3 0 4 5 6 7 8 9]
[1 2 0 3 4 5 6 7 8 9]
[1 2 0 3 4 5 6 7 8 9]
[1 2 0 3 4 5 6 7 8 9]
[1 2 0 3 4 5 6 7 8 9]
[1 2 0 3 4 5 6 7 8 9]
[1 2 0 3 4 5 6 7 8 9]
[1 2 0 3 4 5 6 7 8 9]
Seventh pass:
[1 2 0 3 4 5 6 7 8 9]
[1 2 0 3 4 5 6 7 8 9]
[1 0 2 3 4 5 6 7 8 9]
[1 0 2 3 4 5 6 7 8 9]
[1 0 2 3 4 5 6 7 8 9]
[1 0 2 3 4 5 6 7 8 9]
[1 0 2 3 4 5 6 7 8 9]
[1 0 2 3 4 5 6 7 8 9]
[1 0 2 3 4 5 6 7 8 9]
[1 0 2 3 4 5 6 7 8 9]
Eighth pass:
[1 0 2 3 4 5 6 7 8 9]
[0 1 2 3 4 5 6 7 8 9]
[0 1 2 3 4 5 6 7 8 9]
[0 1 2 3 4 5 6 7 8 9]
[0 1 2 3 4 5 6 7 8 9]
[0 1 2 3 4 5 6 7 8 9]
[0 1 2 3 4 5 6 7 8 9]
[0 1 2 3 4 5 6 7 8 9]
[0 1 2 3 4 5 6 7 8 9]
[0 1 2 3 4 5 6 7 8 9]
Final Sorting:

[0 1 2 3 4 5 6 7 8 9]
8 passes

How many comparisons and how many element moves were used by each method?

72 comparisons
23 element moves

Selection Sort

[2 7 9 4 1 5 3 6 0 8]	9 is largest
[2 7 8 4 1 5 3 6 0 9]	8 is largest
[2 7 0 4 1 5 3 6 8 9]	7 is largest
[2 6 0 4 1 5 3 7 8 9]	6 is largest
[2 3 0 4 1 5 6 7 8 9]	5 is largest
[2 3 0 4 1 5 6 7 8 9]	4 is largest
[2 3 0 1 4 5 6 7 8 9]	3 is largest
[2 1 0 3 4 5 6 7 8 9]	2 is largest
[0 1 2 3 4 5 6 7 8 9]	1 is okay, list is sorted

How many comparisons and how many element moves were used by each method?

8 comparisons
8 element moves






Which is the best performing method for sorting this array of integers? 

Selection sort has the least comparisons and element moves in total. Therefore selection sort is the best performing method for sorting this array of integers.

Which would be the worst arrangement of this sequence?

There would not be the worst arrangement since all three sorting algorithms will take the same amount of comparisons and element moves despite the arrangement of the array.
