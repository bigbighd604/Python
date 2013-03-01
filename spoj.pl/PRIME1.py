#!/usr/bin/env python

import time

prime_list = []


def is_prime(num):
  for i in xrange(len(prime_list)):
    p = prime_list[i]
    if (p * p > num): return True
    if (num % p == 0): return False
  return True


def generate_list():
  prime_list.append(2)
  for i in xrange(3, 32000, 2):
    if is_prime(i):
      prime_list.append(i)


def calculate(start, end):
  result = []
  if (start <= 2):
    result.append(2)
    start = 3
  if (start % 2 == 0): start += 1

  # TODO(andrewlv): only need to check up to sqrt(num) to test prime.
  for i in xrange(start, end + 1, 2):
    if is_prime(i):
      result.append(i)

  return result


if __name__ == '__main__':
 pairs = int(raw_input())
 pair_list = []
 for i in xrange(pairs):
   start, end = raw_input().split()
   pair_list.append((int(start), int(end)))

 generate_list()
 for start, end in pair_list:
   result = calculate(start, end)
   print '\n'.join(map(str, result))
   print ''
