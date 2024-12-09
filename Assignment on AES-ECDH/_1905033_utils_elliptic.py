import math
import random
from sympy import nextprime, Symbol, Eq, solve
def generate_prime(bits):
    prime = nextprime(2 ** (bits - 1))
    return prime

def calculateAB(ka, a, b, p, x1, y1):
    binary_representation = bin(ka)[3:]
    x2 = x1
    y2 = y1
    for i, bit in enumerate(binary_representation):
        (x1, y1) = point_doubling(x1, y1, a, p)
        if bit == '1':
            x1, y1 = point_addition(x1, y1, x2, y2, a, p)
    return x1, y1


def point_doubling(x, y, a, p):
    slope = (3 * x ** 2 + a) * pow(2 * y, -1, p) % p
    x_result = (slope ** 2 - 2 * x) % p
    y_result = (slope * (x - x_result) - y) % p
    return x_result, y_result


def point_addition(x1, y1, x2, y2, a, p):
    slope = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x_result = (slope ** 2 - x1 - x2) % p
    y_result = (slope * (x1 - x_result) - y1) % p
    return x_result, y_result

# def generate_random_prime(bits):
#     while True:
#         potential_prime = random.getrandbits(bits)
#         if all(potential_prime % i != 0 for i in range(2, int(potential_prime ** 0.5) + 1)):
#             return potential_prime

def legendre(a, p):
    return pow(a, (p - 1) // 2, p)

def tonelli(n, p):
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r

def generate(length):
    p = generate_prime(length)
    low = math.floor(p + 1 - 2 * math.sqrt(p))
    high = math.floor(p + 1 + 2 * math.sqrt(p))
    if low != high:
        E = random.randint(low, high)
    else:
        E = low
    ka = random.randint(2, E - 1)
    kb = random.randint(2, E - 1)
    a = 2
    b = 2
    # x1 = 5
    # y1 = 1
    while True:
        x1 = random.randint(1, p - 1)
        expr = (x1 ** 3 + a * x1 + b) % p
        if pow(expr, (p - 1) // 2, p) == 1:
            y1 = pow(expr, (p + 1) // 4, p)
            return p, ka,kb, a, b, x1, y1


def for_alice(length):
    p = generate_prime(length)
    low = math.floor(p + 1 - 2 * math.sqrt(p))
    high = math.floor(p + 1 + 2 * math.sqrt(p))
    if low != high:
        E = random.randint(low, high)
    else:
        E = low

    ka = random.randint(2, E - 1)
    # y^2 = x^3 + ax + b
    a = 2
    b = 2
    # x1 = 5
    # y1 = 1
    while True:
        x1 = random.randint(1, p - 1)
        expr = (x1 ** 3 + a * x1 + b) % p
        if pow(expr, (p - 1) // 2, p) == 1:
            y1 = pow(expr, (p + 1) // 4, p)
            return p, ka, a, b, x1, y1
    # print(x1, y1)
    # return p, ka, a, b, x1, y1


def for_bob(p):
    low = math.floor(p + 1 - 2 * math.sqrt(p))
    high = math.floor(p + 1 + 2 * math.sqrt(p))
    if low != high:
        E = random.randint(low, high)
    else:
        E = low
    kb = random.randint(2, E - 1)
    return kb
