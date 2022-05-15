import math
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

PRIMES = [112272535095293] * 100


# cpu bound, no io
def is_prime(num):
    # num can only be divided by 1 and himself
    if num < 2:
        return False

    if num % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(num)))

    for i in range(3, sqrt_n + 1, 2):
        if num % i == 0:
            return False

    return True


def single_thread():
    for num in PRIMES:
        is_prime(num)


def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print("single thread cost: ", end - start)

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi threads cost: ", end - start)

    start = time.time()
    multi_process()
    end = time.time()
    print("multi process cost: ", end - start)
