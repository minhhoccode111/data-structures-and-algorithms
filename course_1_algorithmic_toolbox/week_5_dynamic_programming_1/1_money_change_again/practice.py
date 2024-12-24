# python3


# practice implementattion


# time: O(n×m): (0  n) × m.length
# space: O(n): store 0  m items
def change(money, coins):
    if money < 0:
        return None

    minNumCoins = [float("inf")] * (money + 1)
    minNumCoins[0] = 0

    for submoney in range(1, money + 1):
        for coin in coins:
            if submoney >= coin:
                minNumCoins[submoney] = min(
                    minNumCoins[submoney - coin] + 1, minNumCoins[submoney]
                )

    return minNumCoins[money]


if __name__ == "__main__":
    money = int(input())
    coins = [5, 4, 1]
    print(change(money, coins))
