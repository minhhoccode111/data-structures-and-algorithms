from change_dp import change


def test():

    # Test cases for change function

    testcases = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 1),
        (4, 1),
        (5, 2),
        (6, 2),
        (7, 2),
        (8, 2),
        (9, 3),
        (10, 3),
        (11, 3),
        (12, 3),
        (13, 4),
        (14, 4),
        (15, 4),
        (16, 4),
        (17, 5),
        (18, 5),
        (19, 5),
        (20, 5),
        (21, 6),
        (22, 6),
        (23, 6),
    ]

    for money, expected in testcases:
        result = change(money)
        print(f"Money: {money}, Expected: {expected}, Got: {result}")
        assert result == expected, f"Test failed for money={money}"

    print("all testcases passed")


test()
