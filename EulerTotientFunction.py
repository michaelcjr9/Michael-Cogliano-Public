import matplotlib.pyplot as plt
import numpy as np


def is_prime(number):
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def find_prime_factors(value):
    prime_factors = []
    for factor in range(2, value + 1):
        if value % factor == 0 and is_prime(factor):
            prime_factors.append(factor)
    return prime_factors


def all_primes_up_to(limit):
    prime_numbers = []
    for candidate in range(2, limit + 1):
        if is_prime(candidate):
            prime_numbers.append(candidate)
    return prime_numbers


def euler_totient_function(n):
    if n == 1:
        return 1
    totient = n
    prime_factors = find_prime_factors(n)
    for prime in prime_factors:
        totient *= 1 - (1 / prime)
    return int(totient)


n_values = np.arange(1, 1000)
totient_values = [euler_totient_function(n) for n in n_values]

plt.scatter(n_values, totient_values, s=1)
plt.xlim([0, max(n_values) + 0.5])
plt.ylim([0, max(totient_values) + 0.5])
plt.xlabel("n")
plt.ylabel("φ(n)")
plt.title("Euler Totient Function")
plt.grid(True)
plt.show()
