"""
To factorise a number, divide it by the first possible prime number.
Take the resulting quotient below the number.
If it is possible, continue dividing this quotient successively by the same prime number.
When you cannot do the division by this prime number, divide it by the next possible prime number.
And so forth until the final quotient is 1.
Finally write this number as a product of powers of prime factors.

"""


def factorise(n):
    if n <= 1:
        return [n]
    facts = []
    p = 2  # p is a prime number
    while n > 1:
        for i in range(2, n+1):
            bol = True
            while bol:
                if n % i == 0:
                    n //= i
                    facts.append(i)
                else:
                    bol = False
    return facts


n = 126
print(factorise(n))