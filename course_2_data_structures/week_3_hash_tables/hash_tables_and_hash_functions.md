# Hash Tables and Hash Functions assignment

1. What is the size of the array needed to store integer keys with up to 1212 digits using direct addressing?

- 10^12

This is the number of all integers with up to 1212 digits.

2. What is the maximum possible chain length for a hash function h(x)=x mod 1000h(x)=xmod1000 used with a hash table of size 10001000 for a universe of all integers with at most 1212 digits?

- 10^9

When the values of the last 33 digits are fixed, there are 109109 numbers with at most 1212 digits.

3. You want to hash integers from 00 up to 10000001000000. What can be a good choice of pp for the universal family?

- 1000003

This is a prime number bigger than 1000000

4. How can one build a universal family of hash functions for integers between −1000000−1000000 (minus one million) and 10000001000000 (one million)?

- First, add 1000000 to each integer and get the range of integers between 0 and 2000000. Then use the universal family for integers with p=2000003
