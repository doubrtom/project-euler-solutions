import time


def is_palindrom(x):
    rev_x = int(str(x)[::-1])
    return x - rev_x == 0


def find_palindrom_version_a():
    """Find palindrom. Basic version."""
    max_palindrome = 0

    for a in range(999, 99, -1):
        for b in range(999, 99, -1):
            mul = a * b
            if is_palindrom(mul) and mul > max_palindrome:
                max_palindrome = mul

    return max_palindrome


def find_palindrom_version_b():
    """Find palindrom. Optimized version.

    Do not test same numbers twice, multiplication is commutative.
    (i.e. 7 * 9 = 9 * 7)
    Stop inner loop at number from previous palindrom.
    """
    max_palindrome = 0
    number_b = 99

    for a in range(999, 99, -1):
        for b in range(a, number_b, -1):
            mul = a * b
            if is_palindrom(mul) and mul > max_palindrome:
                max_palindrome = mul
                number_b = b
                break

    return max_palindrome


def time_versions():
    start_time = time.time()
    max_palindrome_a = find_palindrom_version_a()
    end_time = time.time()
    calculation_a_time = end_time - start_time

    start_time = time.time()
    max_palindrome_b = find_palindrom_version_b()
    end_time = time.time()
    calculation_b_time = end_time - start_time

    print("Max palindrome is a = {}, b = {}".format(
        max_palindrome_a, max_palindrome_b)
    )
    print("Time a = {} s, b = {} s".format(
        calculation_a_time, calculation_b_time)
    )


# time_versions()
print("Max palindrome is {}".format(find_palindrom_version_b()))
