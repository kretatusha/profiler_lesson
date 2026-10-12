import math

def is_prime(num):
    """Checks if num is prime number"""
    for i in range(2, int(math.sqrt(num)) + 1):
        if not num % i:
            return False
    return True

def find_prime_factors(num):
    """Find prime factors of num"""
    result = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if is_prime(i) and not num % i:
            result.append(i)
    return result