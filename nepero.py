#!/usr/bin/env python3

import random
import argparse

parser = argparse.ArgumentParser(description='Nepero number calculation')
parser.add_argument("-n", default=5000, type=int, help="Distribution magnitude")

args = parser.parse_args()
magnitude = args.n

distribution = []

for i in range(magnitude):
    count = 0
    j = 0
    while j <= 1:
        j += random.uniform(0, 1)
        count = count + 1
    distribution.append(count)

nepero = sum(distribution) / len(distribution)
print(nepero)