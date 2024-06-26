def is_prime(num: int) -> bool:
    """determine if a number is prime or not
    Retreived from https://www.pythonpool.com/check-if-number-is-prime-in-python/

    Args:
        num (int): any integer greater than 1

    Returns:
        bool: True if the number is prime; else False
    """
    if num > 1:
        for n in range(2,num): # check each number for a remainer and return False if none
            if (num % n) == 0:
                return False
        return True # return true because we didn't find any remainders
    else:
        return False # the number isn't greater than 1


def print_primes(numbers: range) -> None:
    for num in numbers:
        if is_prime(num):
            print(num)

# don't code it like this ... do your error checking
# isnumeric and/or try/except and maybe an exit(-1)
input_number: int = 0
entry = input('Enter a number greater than 1: ')

# confirm it is an integer
# convert it to an int
print_primes(range(2, input_number))