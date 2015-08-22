"""
Problem

"""

def binize(n):
    b = []
    while n:
        b.append(n & 1)
        n >>= 1
    return b

def negate(bits):
    """
    returns negative of bits in base -2 array where bits is base 2 array

    """
    bits.extend([0, 0])
    signs = [(-1 if y % 2 else 1) for y in range(len(bits))]
    negs = [-b for b in bits]
    bits = [0] * len(bits)
    for i, n in enumerate(negs):
        if not n:
            continue

        if n == signs[i]:
            bits[i] += 1
        else:
            bits[i] += 1
            bits[i+1] += 1

    for i, b in enumerate(bits):
        if not b:
            continue

        while bits[i] >= 2:
            if bits[i+1]:
                bits[i+1] -= 1
                bits[i] -= 2
            else:
                bits[i] -= 2
                bits[i+1] += 1
                bits[i+2] += 1
    return bits


def solution(bits):
    """
    returns negative of bits in base -2 array where bits is base -2 array
    negative of a bit in slot is a bit in the slot and a bit in the next higher slot
    """
    bits.extend([0, 0])
    negs = [0] * len(bits)

    for i, b in enumerate(bits):
        if b:  # add negated
            negs[i] += 1
            negs[i+1] += 1

    for i, n in enumerate(negs):  # normalize
        while negs[i] >= 2:
            if negs[i+1]:  # cancel out
                negs[i] -= 2
                negs[i+1] -= 1
            else:  # shift to higher order bits
                negs[i] -= 2
                negs[i+1] += 1
                negs[i+2] += 1
    return negs

def run(x):
    """
    take in int x and return array of base -2 that is  -x
    """
    bits = binize(x)
    print("{0} = {1}, -{0} = {2}".format(x, bits, solution(bits)))


