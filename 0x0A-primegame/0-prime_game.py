#!/usr/bin/python3
""" 0x0A. Prime Game """


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

    for num in nums[:x]:
        primes = primeNumbers(num)
        # print(f"primes = {primes}")
        turn = 0                    # current player is Maria

        for prime in primes:
            # print(f"{['Maria', 'Ben'][turn % 2]} removed {prime} from {list(range(1, num + 1))}")
            turn += 1

        winner = (turn + 1) % 2     # winner is the other player
        scores[winner] += 1
        # print(f"for list {list(range(1, num + 1))}, winner is {['Maria', 'Ben'][winner]}")

    if scores[0] == scores[1]:
        return None
    return "Maria" if scores[0] > scores[1] else "Ben"


if __name__ == "__main__":
    x = 3
    nums = [4, 5, 1]
    print(f"x = {x}, nums = {nums} -> {isWinner(x, nums)}")
