import functools


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def lcmm(*args):
    return functools.reduce(lcm, args)


number = lcmm(*range(1, 21))

print("Number is {}".format(number))
