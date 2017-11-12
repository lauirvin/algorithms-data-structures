1. Manually arrange the sequence [2 7 9 4 1 5 3 6 0 8] in ascending order using insertion sort, bubble sort
and selection sort, showing at each step the new configuration of the sequence. How many
comparisons and how many element moves were used by each method? Which is the best performing
method for sorting this array of integers? Which would be the worst arrangement of this sequence?

Insertion Sort:

[2 7 9 4 1 5 3 6 0 8]
[2] [7 9 4 1 5 3 6 0 8] 0 Comparisons, 0 moves
[2 7] [9 4 1 5 3 6 0 8]	1 Comparison, 0 moves
[2 7 9] [4 1 5 3 6 0 8]	2 Comparisons, 0 moves
[2 4 7 9] [1 5 3 6 0 8]	5 Comparisons 2 moves
[1 2 4 7 9] [5 3 6 0 8]	9 Comparisons 6 moves 
[1 2 4 5 7 9] [3 6 0 8]	12 Comparisons 8 moves 
[1 2 3 4 5 7 9] [6 0 8]	17 Comparisons 12 moves 
[1 2 3 4 5 6 7 9] [0 8]	20 Comparisons 14 moves 
[0 1 2 3 4 5 6 7 9] [8]	28 Comparisons 22 moves 
[0 1 2 3 4 5 6 7 8 9] 30 Comparisons 23 moves 

[0 1 2 3 4 5 6 7 8 9]

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


Selection Sort

[2 7 9 4 1 5 3 6 0 8]
[2 7 9 4 1 5 3 6 0 8] 1 Comparison, 0 moves
[2 7 9 4 1 5 3 6 0 8] 2 Comparisons, 0 moves
[2 7 9 4 1 5 3 6 0 8] 3 Comparisons, 0 moves
[2 7 9 4 1 5 3 6 0 8] 4 Comparisons, 0 moves
[1 7 9 4 2 5 3 6 0 8] 5 Comparisons, 1 moves
[1 7 9 4 2 5 3 6 0 8] 6 Comparisons, 1 moves
[1 7 9 4 2 5 3 6 0 8] 7 Comparisons, 1 moves
[1 7 9 4 2 5 3 6 0 8] 8 Comparisons, 1 moves
[0 7 9 4 2 5 3 6 1 8] 8 Comparisons, 2 moves
[0 7 9 4 2 5 3 6 1 8] 9 Comparisons, 2 moves
[0 7 9 4 2 5 3 6 1 8] 10 Comparisons, 2 moves
[0 7 9 4 2 5 3 6 1 8] 11 Comparisons, 2 moves
[0 4 9 7 2 5 3 6 1 8] 11 Comparisons, 3 moves
[0 4 9 7 2 5 3 6 1 8] 12 Comparisons, 3 moves
[0 2 9 7 4 5 3 6 1 8] 12 Comparisons, 4 moves
[0 2 9 7 4 5 3 6 1 8] 13 Comparisons, 4 moves
[0 2 9 7 4 5 3 6 1 8] 14 Comparisons, 4 moves
[0 2 9 7 4 5 3 6 1 8] 15 Comparisons, 4 moves
[0 2 9 7 4 5 3 6 1 8] 16 Comparisons, 4 moves
[0 1 9 7 4 5 3 6 2 8] 16 Comparisons, 5 moves
[0 1 9 7 4 5 3 6 2 8] 17 Comparisons, 5 moves
[0 1 9 7 4 5 3 6 2 8] 18 Comparisons, 5 moves
[0 1 7 9 4 5 3 6 2 8] 18 Comparisons, 6 moves
[0 1 7 9 4 5 3 6 2 8] 19 Comparisons, 6 moves
[0 1 4 9 7 5 3 6 2 8] 19 Comparisons, 7 moves
[0 1 4 9 7 5 3 6 2 8] 20 Comparisons, 7 moves
[0 1 4 9 7 5 3 6 2 8] 21 Comparisons, 7 moves
[0 1 3 9 7 5 4 6 2 8] 21 Comparisons, 8 moves
[0 1 3 9 7 5 4 6 2 8] 22 Comparisons, 8 moves
[0 1 3 9 7 5 4 6 2 8] 23 Comparisons, 8 moves
[0 1 2 9 7 5 4 6 3 8] 23 Comparisons, 9 moves
[0 1 2 9 7 5 4 6 3 8] 24 Comparisons, 9 moves
[0 1 2 9 7 5 4 6 3 8] 25 Comparisons, 9 moves
[0 1 2 7 9 5 4 6 3 8] 25 Comparisons, 10 moves
[0 1 2 7 9 5 4 6 3 8] 26 Comparisons, 10 moves
[0 1 2 5 9 7 4 6 3 8] 26 Comparisons, 11 moves
[0 1 2 5 9 7 4 6 3 8] 27 Comparisons, 11 moves
[0 1 2 4 9 7 5 6 3 8] 27 Comparisons, 12 moves
[0 1 2 4 9 7 5 6 3 8] 28 Comparisons, 12 moves
[0 1 2 4 9 7 5 6 3 8] 29 Comparisons, 12 moves
[0 1 2 3 9 7 5 6 4 8] 29 Comparisons, 13 moves
[0 1 2 3 9 7 5 6 4 8] 30 Comparisons, 13 moves
[0 1 2 3 9 7 5 6 4 8] 31 Comparisons, 13 moves
[0 1 2 3 7 9 5 6 4 8] 31 Comparisons, 14 moves
[0 1 2 3 7 9 5 6 4 8] 32 Comparisons, 14 moves
[0 1 2 3 5 9 7 6 4 8] 32 Comparisons, 15 moves
[0 1 2 3 5 9 7 6 4 8] 33 Comparisons, 15 moves
[0 1 2 3 5 9 7 6 4 8] 34 Comparisons, 15 moves
[0 1 2 3 4 9 7 6 5 8] 34 Comparisons, 16 moves
[0 1 2 3 4 9 7 6 5 8] 35 Comparisons, 16 moves
[0 1 2 3 4 9 7 6 5 8] 36 Comparisons, 16 moves
[0 1 2 3 4 7 9 6 5 8] 36 Comparisons, 17 moves
[0 1 2 3 4 7 9 6 5 8] 37 Comparisons, 17 moves
[0 1 2 3 4 6 9 7 5 8] 37 Comparisons, 18 moves
[0 1 2 3 4 6 9 7 5 8] 38 Comparisons, 18 moves
[0 1 2 3 4 5 9 7 6 8] 38 Comparisons, 19 moves
[0 1 2 3 4 5 9 7 6 8] 39 Comparisons, 19 moves
[0 1 2 3 4 5 9 7 6 8] 40 Comparisons, 19 moves
[0 1 2 3 4 5 7 9 6 8] 40 Comparisons, 20 moves
[0 1 2 3 4 5 7 9 6 8] 41 Comparisons, 20 moves
[0 1 2 3 4 5 6 9 7 8] 41 Comparisons, 21 moves
[0 1 2 3 4 5 6 9 7 8] 42 Comparisons, 21 moves
[0 1 2 3 4 5 6 9 7 8] 43 Comparisons, 21 moves
[0 1 2 3 4 5 6 7 9 8] 43 Comparisons, 22 moves
[0 1 2 3 4 5 6 7 9 8] 44 Comparisons, 22 moves
[0 1 2 3 4 5 6 7 9 8] 45 Comparisons, 22 moves
[0 1 2 3 4 5 6 7 8 9] 45 Comparisons, 23 moves

How many comparisons and how many element moves were used by each method?

Insertion Sort: 30 Comparisons, 23 moves 
Bubble Sort: 81 Comparisons, 23 moves
Selection Sort: 45 Comparisons, 23 moves

Which is the best performing method for sorting this array of integers? 

Insertion sort has the least comparisons in total. Therefore insertion sort is the best performing method for sorting this array of integers.

Which would be the worst arrangement of this sequence?

The worst arragement of this sequence would be bubble sort

The worst arragenment of this sequence would be the sorted sequence in reverse.
[9 8 7 6 5 4 3 2 1 0]