#!/usr/bin/python3
""" 0x0A. Prime Game """


def memoize(f):
    """ Memoization decorator """
    cache = {}

    def wrapper(*args):
        """ Memoized function """
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrapper


@memoize
def primeNumbers(n):
    """ Returns a list of prime numbers up to n """
    if n < 2:
        return []

    root = 1
    primes = [2]

    for number in range(2, n + 1):
        isPrime = True
        if root ** 2 < number:
            root += 1

        for k in range(2, root + 1):
            if number % k == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(number)

    return primes


def isWinner(x, nums):
    """ Returns the name of the player that won the most rounds """
    if type(x) is not int or x < 1 or type(nums) is not list:
        return None
    if not all([type(num) is int for num in nums]):
        return None

    scores = [0, 0]                 # Maria, Ben
    all_primes = primeNumbers(max(nums))

    for num in nums[:x]:
        # get the primes up to the current number
        turns = 0
        for prime in all_primes:
            if prime > num:
                break
            turns += 1
        # the players makes optimal moves, so all the primes are removed
        winner = (turns + 1) % 2     # winner is the other player
        scores[winner] += 1

    if scores[0] == scores[1]:
        return None
    return "Maria" if scores[0] > scores[1] else "Ben"
