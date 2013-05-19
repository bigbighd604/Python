#!/usr/bin/env python

#Suppose you have an array of 1001 integers. The integers are in random order,
# but you know each of the integers is between 1 and 1000 (inclusive).
# In addition, each number appears only once in the array, except for
# one number, which occurs twice. Assume that you can access each element
# of the array only once. Describe an algorithm to find the repeated number.
# If you used auxiliary storage in your algorithm, can you find an algorithm
# that does not require it?

import random
import sys

def GenArray(length):
  array = range(1,length + 1)
  dup = random.randint(1, length)
  print 'Dup num generated: %s' % dup
  array.append(dup)
  random.shuffle(array)
  return array

def XorFind(array):
  print 'Start Xor find ...'
  found = 0
  for i, item in enumerate(array):
    found = found ^ item ^ i
  # An alternative:
  #for i in xrange(1, length + 2):
  #  found = found ^ array[i-1] ^ (i - 1)
  print 'Dup num founded (Xor): %s' % found

def SumFind(array):
  print 'Start Sum find ...'
  length = len(array)
  expect_sum = (1 + length - 1) * (length - 1) / 2
  real_sum = reduce(lambda x, y : x + y, array)
  print 'Dup num founded (Sum): %s' % (real_sum - expect_sum)

if __name__ == '__main__':
  length = int(sys.argv[1])
  array = GenArray(length)
  XorFind(array)
  SumFind(array)
