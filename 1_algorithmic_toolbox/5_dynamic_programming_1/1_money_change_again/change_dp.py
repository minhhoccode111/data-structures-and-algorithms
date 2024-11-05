def change(money):
    if money < 0:
        return None
    # first declare a list of coins, desc order
    coins = [4, 3, 1]
    # then find the largest coin in that list of coins
    maxCoin = max(coins)
    # then init a list of infinite float number default value
    # with the length of maxCoin + 1, enough to store from 0 - maxCoin values
    minNumCoins = [float("inf")] * (maxCoin + 1)
    # then we give the base case when money = 0, minNumCoins will = 0 too
    minNumCoins[0] = 0

    # then we loop from 1 to money (0 is already base case)
    for m in range(1, money + 1):
        # reset current position in minNumCoins to infinity to compare min values
        minNumCoins[m % (maxCoin + 1)] = float("inf")
        # then we loop through each coin we have
        # to find if the minimum coins of current m minus coin + 1
        # ex: with m = 23 (result will be 5, which 5 + 5 + 5 + 4 + 4)
        # then we have to find between 3 coins: min(minNumCoins[(23 - 5) % (5 + 1)] + 1, minNumCoins[(23 - 4) % (5 + 1)] + 1, minNumCoins[(23 - 1) % (5 + 1)] + 1)
        for coin in coins:
            # if current m is greater or equal to current coin
            if m >= coin:
                # and the min minNumCoins[m - coin] is the smallest
                if (
                    minNumCoins[(m - coin) % (maxCoin + 1)] + 1
                    < minNumCoins[m % (maxCoin + 1)]
                ):
                    minNumCoins[m % (maxCoin + 1)] = (
                        minNumCoins[(m - coin) % (maxCoin + 1)] + 1
                    )

    return minNumCoins[money % (maxCoin + 1)]


if __name__ == "__main__":
    m = int(input())
    print(change(m))
