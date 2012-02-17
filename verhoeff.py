#!/usr/bin/env python
# Copyright 2012 Christopher Abiad
# Verhoeff algorithm implementation
#
# Based on algorithm description found on Wikipedia:
# https://en.wikipedia.org/wiki/Verhoeff_algorithm @2012-02-16@19:23EST
#
# With further reference at: http://www.cs.utsa.edu/~wagner/laws/verhoeff.html
#
# Checksum digits are assumed by the last digit of the passed in argument

__author__ = 'Chris Abiad'

import argparse

# D5 'multiplication' table
d = (
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
        (1, 2, 3, 4, 0, 6, 7, 8, 9, 5),
        (2, 3, 4, 0, 1, 7, 8, 9, 5, 6),
        (3, 4, 0, 1, 2, 8, 9, 5, 6, 7),
        (4, 0, 1, 2, 3, 9, 5, 6, 7, 8),
        (5, 9, 8, 7, 6, 0, 4, 3, 2, 1),
        (6, 5, 9, 8, 7, 1, 0, 4, 3, 2),
        (7, 6, 5, 9, 8, 2, 1, 0, 4, 3),
        (8, 7, 6, 5, 9, 3, 2, 1, 0, 4),
        (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
    )

# Inverses of d5
# (In other words, for any j, inv[j] is value for which d[j][inv[j]] == 0)
inv = (0, 4, 3, 2, 1, 5, 6, 7, 8, 9)

# Special permutations required to catch all adjacent transpositions
# Precalculated for time efficiency, but p can be calculated as follows
# p = [
#         (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
#         (1, 5, 7, 6, 2, 8, 3, 0, 9, 4),
#     ]
# for i in range(2, 8):
#     row = []
#     for j in range(0, 10):
#         row.append(p[i-1][p[1][j]])
#     p.append(tuple(row))
# p = tuple(p)
p = ((0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
     (1, 5, 7, 6, 2, 8, 3, 0, 9, 4),
     (5, 8, 0, 3, 7, 9, 6, 1, 4, 2),
     (8, 9, 1, 6, 0, 4, 3, 5, 2, 7),
     (9, 4, 5, 3, 1, 2, 6, 8, 7, 0),
     (4, 2, 8, 6, 5, 7, 3, 9, 0, 1),
     (2, 7, 9, 3, 8, 0, 6, 4, 1, 5),
     (7, 0, 4, 6, 9, 1, 3, 2, 5, 8))


def calculate_verhoeff(integer):
    check = 0
    digit_list = [int(char) for char in str(integer)]
    digit_list.reverse()
    # Iterate over digits in integer by iterating over string
    for i in range(0, len(digit_list)):
        check = d[check][
            p[i % 8][digit_list[i]]
        ]
    return str(integer) + str(inv[check])


def validate_verhoeff(integer):
    check = 0
    digit_list = [int(char) for char in str(integer)]
    digit_list.reverse()
    # Iterate over digits in integer by iterating over string
    for i in range(0, len(digit_list)):
        check = d[check][
            p[i % 8][digit_list[i]]
        ]
    if check == 0:
        return True
    return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""By default, calculate a Verhoeff checksum for a number.
With the '-d' argument, instead validate a Verhoeff checksummed value.""")
    parser.add_argument(
        'integers', metavar='N', type=int, nargs='+',
        help='integer to calculate or validate the Verhoeff checksum of')
    parser.add_argument(
        '-v', '--validate', dest='action', action='store_const',
        const=validate_verhoeff, default=calculate_verhoeff,
        help="validate the integer's Verhoeff checksum "
        "(default: calculate the Verhoeff checksum)")
    args = parser.parse_args()
    for integer in args.integers:
        print args.action(integer)
