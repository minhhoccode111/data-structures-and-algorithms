# Dynamic programming 1

## Change problem

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

Pseudo code with dynamic programming algorithm

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
