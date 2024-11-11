from lcm import lcm


def test_lcm():
    # Basic tests
    assert lcm(1, 1) == 1
    assert lcm(1, 2) == 2
    assert lcm(2, 3) == 6
    assert lcm(4, 5) == 20
    assert lcm(6, 8) == 24

    # Edge cases with 0
    assert lcm(0, 10) == 0
    assert lcm(10, 0) == 0
    assert lcm(0, 0) == 0

    # Small prime numbers
    assert lcm(2, 3) == 6
    assert lcm(3, 5) == 15
    assert lcm(5, 7) == 35
    assert lcm(7, 11) == 77

    # Composite numbers
    assert lcm(4, 10) == 20
    assert lcm(9, 15) == 45
    assert lcm(12, 18) == 36
    assert lcm(14, 21) == 42

    # Large numbers
    assert lcm(1000000, 1000000) == 1000000
    assert lcm(1000000, 2000000) == 2000000
    assert lcm(123456, 654321) == 26926617792
    assert lcm(999999, 888888) == 7999992
    assert lcm(123456789, 987654321) == 13548070123626141

    # Very large numbers
    assert lcm(10**6, 10**7) == 10**7
    assert lcm(10**12, 10**15) == 10**15
    assert lcm(10**18, 10**9) == 10**18
    assert lcm(9999991, 99999989) == 999998800000099
    assert lcm(2**20, 3**15) == 1977326743040

    # Mixed cases with multiples
    assert lcm(12, 30) == 60
    assert lcm(18, 24) == 72
    assert lcm(21, 6) == 42
    assert lcm(33, 77) == 231
    assert lcm(9, 10) == 90

    # Sequential numbers
    assert lcm(29, 30) == 870
    assert lcm(101, 103) == 10403
    assert lcm(199, 200) == 39800

    print("All test cases passed!")


test_lcm()
