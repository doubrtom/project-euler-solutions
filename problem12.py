import math
import itertools
from collections import defaultdict


def create_prime_list(n):
	prime_list = defaultdict(int)

	while n % 2 == 0:
		prime_list[2] += 1
		n //= 2

	for i in range(3, int(math.sqrt(n)), 2):
		while n % i == 0:
			prime_list[i] += 1
			n //= i

	if n > 2:
		prime_list[n] += 1

	return prime_list


def get_factor_count(prime_list):
	count = 1

	for prime, exp in prime_list.items():
		count *= exp + 1

	return count


triangl_number = 1

for i in itertools.count(2):
	triangl_number += i
	prime_list = create_prime_list(triangl_number)
	factor_count = get_factor_count(prime_list)

	if factor_count > 500:
		print(factor_count)
		print(triangl_number)
		break
