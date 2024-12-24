# python3


# computer the minimum number of coins needed to change the given value into
# coins with denominations 1, 3, 4


def change(money, coins):
    if money < 0:
        return None
    maxCoin = max(coins)
    minNumCoins = [0] * (maxCoin + 1)
    minNumCoins[0] = 0

    for submoney in range(1, money + 1):
        minNumCoins[submoney % (maxCoin + 1)] = float("inf")
        for coin in coins:
            if submoney >= coin:
                minNumCoins[submoney % (maxCoin + 1)] = min(
                    minNumCoins[(submoney - coin) % (maxCoin + 1)] + 1,
                    minNumCoins[submoney % (maxCoin + 1)],
                )

    return minNumCoins[money % (maxCoin + 1)]


if __name__ == "__main__":
    m = int(input())
    coins = [4, 3, 1]
    print(change(m, coins))
