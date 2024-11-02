# Change Money Assignment

1. What is the smallest amount of money for which greedy strategy fails with coin denominations of 1, 8, and 20?

- 25

2. What is the minimum number of coins needed to change 32 into with denominations 1, 8, 20?

- 4

32 = 8 + 8 + 8 + 8

3. What is the running time of the dynamic programming algorithm to change m using n different coin

- O(nm)

For each value up to m, we need to try to start changing it with each of n coin denominations, thus the running time is O(nm)

4. Is it possible to change 997 using coins with demoninations 2, 4, and 8?

- No

Proof by contradiction. If it was possible to change 997 using only coins of denominations 2, 4, and 8, it would mean that 2 divides 997, because 2 divides 2, 4, and 8. However, 2 does not divide 997, which is a contradiction
