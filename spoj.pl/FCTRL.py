#!/usr/bin/env python
#
# https://www.spoj.pl/problems/FCTRL
#


def GetZeros(number):
  zeros = 0
  value = 5
  counter = 0

  while value <= number:
    value *= 5
    counter += 1

  for i in xrange(1, counter+1):
    zeros += number / (5 ** i)

  return zeros


if __name__ == '__main__':
  num = int(raw_input())
  numbers = []
  results = []

  for i in xrange(num):
    numbers.append(int(raw_input()))

  for i in numbers:
    results.append(GetZeros(i))

  print '\n'.join([str(result) for result in results])
