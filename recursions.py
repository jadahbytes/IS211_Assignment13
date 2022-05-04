# Part I - Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Part II - Euclid's GCD Algorithm

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


# Part III - String Comparison

def compareTo(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 0
    elif len(s1) == 0:
        return -1
    elif len(s2) == 0:
        return 1

    if s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])


if __name__ == '__main__':
    print(fibonacci(27))
    print(gcd(17, 85))
    print(compareTo('sTring', 'string'))
