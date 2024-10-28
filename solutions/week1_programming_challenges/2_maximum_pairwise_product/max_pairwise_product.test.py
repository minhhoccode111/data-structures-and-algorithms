from max_pairwise_product import max_pairwise_product


def test_cases():
    # generate by ChatGPT
    assert max_pairwise_product([1, 2, 3]) == 6
    assert max_pairwise_product([100, 900, 50, 800]) == 720000
    assert max_pairwise_product([-1, -2, -3, -4]) == 2
    assert max_pairwise_product([-10, 5, 3, 7]) == 35
    assert max_pairwise_product([1, 5, 5]) == 25
    assert max_pairwise_product([3, 7]) == 21
    assert max_pairwise_product([2, 2, 2, 2]) == 4
    assert max_pairwise_product([i for i in range(1, 1000001)]) == 999999000000
    print("All test cases passed!")


test_cases()
