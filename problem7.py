size = 1000000
prime_flags = [True] * size


for i in range(2, size, 1):
    if not prime_flags[i]:
        continue
    for j in range(2*i, size, i):
        prime_flags[j] = False


counter = 0
index = 0


for i in range(2, size):
    if prime_flags[i]:
        counter += 1
    if counter == 10001:
        index = i
        break

print("Founded prime number is {} on the position {}".format(index, counter))
