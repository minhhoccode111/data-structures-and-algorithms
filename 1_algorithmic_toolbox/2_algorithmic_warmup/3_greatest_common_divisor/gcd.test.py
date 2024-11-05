from gcd import gcd


def test_gcd():
    # Test cases where one number is zero
    assert gcd(0, 5) == 5, "Test case gcd(0, 5) failed"
    assert gcd(7, 0) == 7, "Test case gcd(7, 0) failed"
    assert gcd(0, 0) == 0, "Test case gcd(0, 0) failed"

    # Test cases with one as one of the numbers
    assert gcd(1, 7) == 1, "Test case gcd(1, 7) failed"
    assert gcd(7, 1) == 1, "Test case gcd(7, 1) failed"

    # Test cases with equal numbers
    assert gcd(5, 5) == 5, "Test case gcd(5, 5) failed"

    # Test standard cases
    assert gcd(54, 24) == 6, "Test case gcd(54, 24) failed"
    assert gcd(48, 18) == 6, "Test case gcd(48, 18) failed"
    assert gcd(101, 10) == 1, "Test case gcd(101, 10) failed"  # prime and non-prime

    # Test with larger numbers
    assert gcd(270, 192) == 6, "Test case gcd(270, 192) failed"
    assert gcd(100000, 25000) == 25000, "Test case gcd(100000, 25000) failed"

    print("All GCD test cases passed!")


# Call the test function
test_gcd()
