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

def number_to_words(num):
    """
    Convert a number into its word form.
    :param num: Integer to convert
    :return: Word representation of the number
    """
    if num == 0:
        return "zero"

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]

    def wordify(n):
        if n < 10:
            return ones[n]
        elif 10 < n < 20:
            return teens[n - 10]
        elif n >= 10 and n < 100:
            return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
        elif n < 1000:
            return ones[n // 100] + " hundred" + (" " + wordify(n % 100) if n % 100 != 0 else "")
        return ""

    words = ""
    if num < 0:
        words += "minus "
        num = abs(num)

    chunk_count = 0
    while num > 0:
        chunk = num % 1000
        if chunk != 0:
            prefix = wordify(chunk) + (" " + thousands[chunk_count] if thousands[chunk_count] else "")
            words = prefix + (" " + words if words else "")
        num //= 1000
        chunk_count += 1

    return words.strip()

# Example usage
start_number = 10
end_number = 50
prime_numbers = primes_between(start_number, end_number)
print(f"Prime numbers between {start_number} and {end_number}: {prime_numbers}")

number = 123
print(f"The number {number} in words is: '{number_to_words(number)}'")
