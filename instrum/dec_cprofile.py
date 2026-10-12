import cProfile

from euler3 import find_prime_factors


def profile(func):
    """Decorator for run function profile"""
    def wrapper(*args, **kwargs):
        profile_filename = func.__name__ + '.prof'
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        return result
    return wrapper


@profile
def get_prime_numbers():
    find_prime_factors(347389473984)

get_prime_numbers()