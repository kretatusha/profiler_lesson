import time

from euler3 import find_prime_factors

start = time.time()
num=600851475143
prime_factors = find_prime_factors(num)
print("Time: %.03f s" % (time.time() - start))

