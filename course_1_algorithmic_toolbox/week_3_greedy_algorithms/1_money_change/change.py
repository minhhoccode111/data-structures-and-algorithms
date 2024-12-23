# python3

# Compute the minimum number of coins needed to change the given value into
# coins with denominations 1, 5, and 10.


# long solution
def long_change(money):
    numCoins = 0
    # while current money is still greater than 0
    while money > 0:
        if money >= 10:
            money -= 10
        elif money >= 5:
            money -= 5
        else:
            money -= 1
        # increase coins to count
        numCoins += 1
    return numCoins


# one liner
# money // 10: number of 10 bills
# (money % 10) // 5: the remaining of the above to get number of 5 bills
# (money % 5): the remaining of the above to get number of 1 bills
def short_change(money):
    return money // 10 + (money % 10) // 5 + (money % 5)


if __name__ == "__main__":
    m = int(input())
    print(short_change(m))
