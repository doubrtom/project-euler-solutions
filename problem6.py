sum_of_the_squares = 0
square_of_the_sum = 0

for i in range(1, 101):
    sum_of_the_squares += i ** 2
    square_of_the_sum += i

square_of_the_sum = square_of_the_sum ** 2

diff = square_of_the_sum - sum_of_the_squares

print("Sum is {}".format(diff))
