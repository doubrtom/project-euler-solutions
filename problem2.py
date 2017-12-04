UPPER_LIMIT = 4000000
sum = 0

a, b = 1, 2

while True:
    if b % 2 == 0:
        sum += b
    a, b = b, a + b
    if b >= UPPER_LIMIT:
        break

print("Sum is {}".format(sum))
