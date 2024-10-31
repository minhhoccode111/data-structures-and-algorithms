# Linear Search and Binary Search Assignment

1. You have an array with 1023 numbers. You use linear search to determine whether number 239 is in this array or not. How many elements of the array will you look at if number 239 is not present in the array?

- 1023

You will have to look at all the numbers in the array.

2. Can you use binary search to find number 8 in the array [1, 24, 25, 23, 17, 8, 9]?

- No, you cannot.

The array must be sorted before you can apply binary search. 23 < 17, so the array is not sorted.

3. You have a sorted array with 1023 elements. You use binary search to determine whether number 239 is present in this array or not. How many elements of the array will you compare it with if number 239 is not present in this array?

- 10

You will only need to compare 239 with 10 elements of the array, because 10 is roughly the binary logarithm of 1023. For example, if 239 is smaller than all the numbers in the array, you will first compare it with the element with index 511 (starting from 0), then the element with index 255, then with elements with indices 127, 63, 31, 15, 7, 3, 1 and 0 before you determine that 239 is smaller than all numbers in the array.

4. What is the maximum number of iterations a binary search will make to find some number in the array [1, 2, 3, 5, 8, 13, 21, 34]?

- 4

- If we search for number 34, we will first compare it with the number 5 in the middle, then with the number 13 in the middle of the right half, then with the number 21, and then with the number 34. This is because when we have even number of elements we compare with the left of the two middle elements. If we compared with the right of the two middle elements, then to find number 1 we would compare it first with number 8, then with number 3, then with number 2 and then with number 1 - also 4 comparisons.
