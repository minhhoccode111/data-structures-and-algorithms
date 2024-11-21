# Dynamic programming 1

5 easy steps

- define subproblems
- guess part of solution
- recurrence
- recurse + memoize / check acyclic
- solve original problem

## Change problem

Find the minimum number of coins needed to make change

- input: an integer money and an array `COINS` of `d` positive integers
- output: the minimum number of coins with denominations `COINS` that changes `money`

Pseudo code with greedy algorithm

```
GreedyChange(money)
change <- empty collection of coins
while money > 0:
    coin <- largest denomination that does not exceed money
    add coin to change
    money <- money - coin
return change
```

Pseudo code with greedy algorithm

```
RecursiveChange(money, coins)
if money = 0
    return 0
minNumCoins <- Infinity
for i <- 1 to |coins|
    if money >= coin<i>
        numCoins <- RecursiveChange(money - coin<i>, coins)
        if numCoins + 1 < minNumCoins
            minNumCoins <- numCoins + 1
return minNumCoins

```

Ex 1: Use dynamic programming to fill `money` values from 0 to 23 of `MinNumCoins` with `coins = (1, 4, 5)`

```
            m  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
MinNumCoins(m) 0 1 2 3 1 1 2 3 2 2 2  3  3  3  3  3  4  4  4  4  4  5  5  5
```

Pseudo code with dynamic programming algorithm with runtime O(money\*|COINS|)

```
DPChange(money, coins)
MinNumCoins(0) <- 0
for m from 1 to money:
    MinNumCoins(m) <- Infinity
    for i from 1 to |coins|:
        if m >= coin<i>:
            NumCoins <- MinNumCoins(m - coin<i>) + 1
            if NumCoins < MinNumCoins(m):
                MinNumCoins(m) <- NumCoins
return MinNumCoins(money)
```

If money = 10 ^ 9, `DPChange` requires a huge array of size 10 ^ 9. Modify the `DPChange` algorithm so that the array size required does not exceed the value of the largest coin denomination

```
DPChangeLimited(money, COINS)
MaxCoin ← maximum value in COINS
MinNumCoins[0...MaxCoin] ← ∞
MinNumCoins(0) ← 0

for m ← 1 to money
    for each coin in COINS
        if m ≥ coin
            if MinNumCoins((m - coin) mod (MaxCoin + 1)) + 1 < MinNumCoins(m mod (MaxCoin + 1))
                MinNumCoins(m mod (MaxCoin + 1)) ← MinNumCoins((m - coin) mod (MaxCoin + 1)) + 1

return MinNumCoins(money mod (MaxCoin + 1))
```

Modify that function so it not only return the min number of coins but also return what these coins are

```
DPChangeLimited(money, COINS)**
    MaxCoin ← maximum value in COINS
    MinNumCoins[0...MaxCoin] ← ∞
    MinNumCoins(0) ← 0
    CoinsUsed[0...MaxCoin] ← empty list

    for m ← 1 to money
        for each coin in COINS
            if m ≥ coin
                if MinNumCoins((m - coin) mod (MaxCoin + 1)) + 1 < MinNumCoins(m mod (MaxCoin + 1))
                    MinNumCoins(m mod (MaxCoin + 1)) ← MinNumCoins((m - coin) mod (MaxCoin + 1)) + 1
                    CoinsUsed(m mod (MaxCoin + 1)) ← CoinsUsed((m - coin) mod (MaxCoin + 1)) + [coin]

    return MinNumCoins(money mod (MaxCoin + 1)), CoinsUsed(money mod (MaxCoin + 1))
```

## String comparison

- dag: directed acyclic graphs
