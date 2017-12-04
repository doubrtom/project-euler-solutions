max_prime = 0
number = 600851475143
factor = 2

while number != 1:
    if number % factor == 0:
        number //= factor
        max_prime = max(max_prime, factor)
    else:
        factor += 1

print("Max primer number is {}".format(max_prime))
