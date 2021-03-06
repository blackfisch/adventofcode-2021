#!/usr/bin/env python3

'''
The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
'''


def get_common_bits(input: list) -> dict:
    '''
        this solution is hacky again.
        the key of amounts dict is actually the index of the bit in the binary number
        the value is another dict, containing keys '1' and '0' (binary value) with the
        number of times it appears in the index of the bit
    '''
    amounts = {}
    for line in input:
        digits = list(line)  # split strings into single (binary) digits

        for i, d in enumerate(digits):
            place = amounts.get(i, {})
            amount = place.get(d, 0)

            place[d] = amount + 1
            amounts[i] = place
    return amounts


if __name__ == '__main__':
    diag_report = open('input.txt').read().splitlines()

    gamma = ''
    epsilon = ''

    amounts = get_common_bits(diag_report)
    # iterate over dicts to build gamma & epsilon
    for v in amounts.values():
        zeros, ones = v['0'], v['1']

        if zeros > ones:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    # convert strings to integer interpreting as binary
    gamma = int(gamma, base=2)
    epsilon = int(epsilon, base=2)

    print(
        f'Gamma: {gamma}, Epsilon: {epsilon} - Power Consumption: {gamma*epsilon}')
