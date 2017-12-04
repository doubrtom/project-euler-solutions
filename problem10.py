size = 2000001
prime_flags = [True] * size


for i in range(2, size):
    if not prime_flags[i]:
        continue
    for j in range(2*i, size, i):
        prime_flags[j] = False


sum_of_primes = sum(x for x in range(2, size) if prime_flags[x])
print("Sum is {}".format(sum_of_primes))
