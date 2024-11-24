from math import sqrt


def get_primes(num_list):
    for num in num_list:
        if num < 2:
            continue
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))