#!/usr/bin/python3

def primeNumbers(n):
    """ Returns a list of prime numbers up to n """
    root = 1
    primes = []

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
    if type(x) is not int or x < 1:
        return None
    if type(nums) is not list:
        return None
    if not all([type(num) is int for num in nums]):
        return None
    if not all([num > 0 for num in nums]):
        return None

    scores = (0, 0)
    players = ("Maria", "Ben")

    for num in nums:
        primes = primeNumbers(num)
        currentPlayer = 0                   # current player is Maria

        for prime in primes:
            currentPlayer = (currentPlayer + 1) % 2

        winner = (currentPlayer + 1) % 2    # winner is the other player
        scores[winner] += 1

    if scores[0] == scores[1]:
        return None
    return players[scores.index(max(scores))]
