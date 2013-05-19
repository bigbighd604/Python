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
import timeit

class FindDuplicate(object):
  array = None

  @classmethod
  def GenArray(cls, length):
    if cls.array:
      return cls.array
    else:
      array = range(1,length + 1)
      dup = random.randint(1, length)
      print 'Dup num generated: %s' % dup
      array.append(dup)
      random.shuffle(array)
      cls.array = array
      return cls.array

  # By exploiting the following fact:
  # a ^ a = 0
  # 0 ^ a = a
  # This XorFind use one extra storage space.
  # In place modification of array uses no extra space.
  @classmethod
  def XorFind(cls, info=False):
    found = 0
    for i, item in enumerate(cls.array):
      found = found ^ item ^ i
    # An alternative:
    #for i in xrange(1, length + 2):
    #  found = found ^ array[i-1] ^ (i - 1)
    if info:
      print 'Dup num founded (Xor): %s' % found

  # May overflow when dealing with huge array.
  @classmethod
  def SumFind(cls, info=False):
    length = len(cls.array)
    expect_sum = (1 + length - 1) * (length - 1) / 2
    real_sum = reduce(lambda x, y : x + y, cls.array)
    if info:
      print 'Dup num founded (Sum): %s' % (real_sum - expect_sum)

  @classmethod
  def AbsFind(cls, info=False):
    array = cls.array[:]
    for i in xrange(len(array)):
      if array[abs(array[i])] > 0:
        array[abs(array[i])] = - array[abs(array[i])] 
      else:
        if info:
          print 'Dup num found (Abs): %s' % abs(array[i])
        break

if __name__ == '__main__':
  length = int(sys.argv[1])
  num = int(sys.argv[2])
  FindDuplicate.GenArray(length)
  FindDuplicate.XorFind(info=True)
  FindDuplicate.SumFind(info=True)
  FindDuplicate.AbsFind(info=True)
  print 'Xor: %s' % timeit.timeit(FindDuplicate.XorFind, number = num)
  print 'Sum: %s' % timeit.timeit(FindDuplicate.SumFind, number = num)
  print 'Abs: %s' % timeit.timeit(FindDuplicate.AbsFind, number = num)
