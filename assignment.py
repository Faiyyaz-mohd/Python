def is_prime(num):
    """
    Check if a number is prime.
    :param num: Integer to check for primality
    :return: True if the number is prime, False otherwise
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_between(start, end):
    """
    Generate all prime numbers between two given numbers.
    :param start: Starting number (inclusive)
    :param end: Ending number (exclusive)
    :return: List of prime numbers between start and end
    """
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage
start_number = 10
end_number = 50
prime_numbers = primes_between(start_number, end_number)
print(f"Prime numbers between {start_number} and {end_number}: {prime_numbers}")
