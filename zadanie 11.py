import math

def prime_numbers(N: int) -> list:
    """
    Returns a list of all prime numbers from 2 to N.
    """
    list_of_numbers = []
    
    for devendend in range(2, N + 1):
        is_prime = True
        for divisor in range(2, int(math.sqrt(devendend)) + 1):
            if devendend % divisor == 0:
                is_prime = False
                break
        if is_prime:
            list_of_numbers.append(devendend)

    return list_of_numbers


N = int(input())
print(prime_numbers(N))
