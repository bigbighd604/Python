#!/usr/bin/env python
#
# Q. Given length n, number of binary sequences without consecutive 0s.
# Requirement:
# 1. Time complexity - O(n)
#
# i.e. give a length 4 binary, valid sequences are:
# 1111, 0111, 1011, 1101, 1110, 0101,1010, 0110
#


def GetNonContinuousZero(size):
  start_with_zero = [0 for i in xrange(size + 1)]
  start_with_one = [0 for i in xrange(size + 1)]
  start_with_zero[1] = 1
  start_with_one[1] = 1
  for i in xrange(2, size + 1):
    start_with_zero[i] = start_with_one[i - 1]
    start_with_one[i] = start_with_one[i - 1] + start_with_zero[i - 1]
  return start_with_zero[size] + start_with_one[size]

if __name__ == "__main__":
  for n in xrange(1,64):
    print 'Length: %s Non continuous 0: %s' % (n, GetNonContinuousZero(n))
