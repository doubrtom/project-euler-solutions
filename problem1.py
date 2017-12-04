UPPER_LIMIT = 1000

sum_of_numbers = sum(
    x for x in range(UPPER_LIMIT) if (x % 5 == 0 or x % 3 == 0)
)

print("Sum is: {}".format(sum_of_numbers))
