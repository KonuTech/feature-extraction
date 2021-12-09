import time
from functools import wraps


def timeit(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        start_time = time.time()
        result = f(*args, **kwds)
        elapsed_time = time.time() - start_time
        print(f"Elapsed computation time: {elapsed_time:.3f} secs")
        return (elapsed_time, result)

    return wrapper

# @timeit
