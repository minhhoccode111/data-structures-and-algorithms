def change(money):
    numCoins = 0
    while money > 0:
        if money >= 10:
            money -= 10
        elif money >= 5:
            money -= 5
        else:
            money -= 1
        numCoins += 1
    return numCoins


if __name__ == "__main__":
    m = int(input())
    print(change(m))
