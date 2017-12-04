SUM_OF_NUMBERS = 1000

for c in range(3, SUM_OF_NUMBERS):
    for b in range(2, c):
        a = SUM_OF_NUMBERS - c - b
        a2_plus_b2 = a ** 2 + b ** 2
        c2 = c ** 2
        sum_of_numbers = a + b + c
        if a2_plus_b2 == c2 and sum_of_numbers == SUM_OF_NUMBERS:
            print("Product is {}".format(a * b * c))
            exit(0)
