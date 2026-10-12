from line_profiler import profile

import math

def is_prime(num):
    """Checks if num is prime number"""
    for i in range(2, int(math.sqrt(num)) + 1):
        if not num % i:
            return False
    return True

@profile
def find_prime_factors(num):
    """Find prime factors of num"""
    result = []
    for i in range(1, int(math.sqrt(num)) + 1):
        # if is_prime(i) and not num % i:
        if not num % i and is_prime(i):
            result.append(i)
    return result

@profile
def do_some_action():
    find_prime_factors(347389473984)

do_some_action()

# kernprof -l instrum.line_profiler_example.py - run statistic

# Inspect results with:
# python -m line_profiler -rmt line_profiler_example.py.lprof