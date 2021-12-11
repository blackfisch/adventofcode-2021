#!/usr/bin/env python3

'''
As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

For example, suppose you had the following report:

199
200
208
210
200
207
240
269
260
263

This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)

In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?

-> input.txt contains the input data
'''


def get_larger(input: list) -> int:
    larger = 0
    for i in range(1, len(input)):
        # +1, because last element is not selected
        prev_el, cur_el = input[i-1:i+1]
        if cur_el > prev_el:
            larger += 1  # if current element is larger than previous, add 1 to output var
    return larger


if __name__ == '__main__':
    # read each line as array element
    measurements = open('input.txt').read().splitlines()
    # convert every element to integer
    measurements = list(map(int, measurements))
    # print results
    print(f'{get_larger(measurements)} elements were larger than their previous')
