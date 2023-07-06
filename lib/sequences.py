#!/usr/bin/env python3


def print_fibonacci(length):
    if length == 0:
        print("[]")
        return
    sequence = []
    a, b = 0, 1

    while len(sequence) < length:
        sequence.append(a)
        a, b = b, a + b

    print(sequence)
