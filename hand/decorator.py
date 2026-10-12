"""Collect profiling statistic into graphite"""
import time

import euler3


def stats(name):
    """Decorator for send stats to graphite"""

    def _timing(func):
        def _wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = (time.time() - start) * 1000  # msec
            message = '%s %d %d\n' % (name, duration, time.time())

            print(message)

            return result

        return _wrapper

    return _timing


@stats("find_prime_action")
def do_some_action():
    """Doing some useful action"""
    euler3.find_prime_factors(347389473984)

do_some_action()