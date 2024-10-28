from fibonacci_last_digit import fibonacci_last_digit


def test():

    # Basic cases
    assert fibonacci_last_digit(0) == 0
    assert fibonacci_last_digit(1) == 1
    assert fibonacci_last_digit(2) == 1
    assert fibonacci_last_digit(3) == 2
    assert fibonacci_last_digit(4) == 3
    assert fibonacci_last_digit(5) == 5
    assert fibonacci_last_digit(6) == 8
    assert fibonacci_last_digit(7) == 3
    assert fibonacci_last_digit(8) == 1
    assert fibonacci_last_digit(9) == 4
    assert fibonacci_last_digit(10) == 5

    # Edge cases with known large values in Fibonacci series
    assert fibonacci_last_digit(50) == 5
    assert fibonacci_last_digit(100) == 5
    assert fibonacci_last_digit(500) == 5
    assert fibonacci_last_digit(1000) == 5

    # High values to check for efficiency and correctness with mod
    assert fibonacci_last_digit(10000) == 5
    assert fibonacci_last_digit(100000) == 5
    # assert fibonacci_last_digit(1000000) == 5
    # assert fibonacci_last_digit(10000000) == 5
    # assert fibonacci_last_digit(100000000) == 5

    # Random middle-range cases
    assert fibonacci_last_digit(20) == 5
    assert fibonacci_last_digit(21) == 6
    assert fibonacci_last_digit(25) == 5
    assert fibonacci_last_digit(30) == 0
    assert fibonacci_last_digit(35) == 5
    assert fibonacci_last_digit(40) == 5
    assert fibonacci_last_digit(45) == 0

    # # Very high values for stress testing
    # assert fibonacci_last_digit(99999) == 5
    assert fibonacci_last_digit(999999) == 6  # coursera last testcase
    # assert fibonacci_last_digit(9999999) == 5
    # assert fibonacci_last_digit(99999999) == 5
    # assert fibonacci_last_digit(123456789) == 5

    print("All tests passed!")


test()
