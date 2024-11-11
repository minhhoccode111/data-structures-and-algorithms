# Sorting Assignment

1. What is the running time of selecting the minimum element on each iteration of the selection sort?

- O(n)

Selecting the minimum of O(n)O(n) elements is O(n)O(n)

2. Can we use the merging procedure from the lectures to merge the arrays [1, 3, 2, 5, 4] and [5, 6, 7, 8, 9] in order to receive a sorted array?

- No

Both arrays must be sorted prior to merging

3. How many operations are needed to merge two sorted arrays of sizes mm and nn respectively?

- O(n+m)

Merge works in O(n+m)

4. Can you use Count Sort to sort an array of positive real numbers which are less than 100, such as [0.572, 0.25, 2.34, 3.14159, 2.781828, 42], in O(n)O(n) time?

- No

Although the numbers in the array are bounded, Count Sort is not applicable, because it can only be applied to integer numbers: real numbers cannot play the role of indices of an array
