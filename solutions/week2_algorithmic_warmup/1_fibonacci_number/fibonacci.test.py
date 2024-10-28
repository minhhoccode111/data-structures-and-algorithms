from fibonacci import fibonacci_number


def test_fibonacci():
    # Test the base cases
    assert fibonacci_number(0) == 0, "Test case 0 failed"
    assert fibonacci_number(1) == 1, "Test case 1 failed"

    # Test small numbers
    assert fibonacci_number(2) == 1, "Test case 2 failed"
    assert fibonacci_number(3) == 2, "Test case 3 failed"
    assert fibonacci_number(4) == 3, "Test case 4 failed"
    assert fibonacci_number(5) == 5, "Test case 5 failed"

    # Test larger numbers
    assert fibonacci_number(10) == 55, "Test case 10 failed"
    assert fibonacci_number(15) == 610, "Test case 15 failed"

    # Test a larger input to verify scalability
    assert fibonacci_number(20) == 6765, "Test case 20 failed"

    print("All test cases passed!")


# Call the test function
test_fibonacci()
