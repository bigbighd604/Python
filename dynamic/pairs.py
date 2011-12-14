#!/usr/bin/env python
#
# Q. Find the number of correct parenthesis sequence of length 2*n
# Requirements:
# 1. Time complexity - O(n^2)
#
# i.e.
# length 2*3, number is 5: ()()(), (())(), ()(()), (()()), ((()))
#


import copy


# This is not the correct answer
# The result has duplicated combinations
def RecursiveCalculate(left, right):
  # copy.copy only copies direct object reference, not second level
  left_copy = copy.deepcopy(left)
  first = left_copy.pop(0)
  if first[1] == right:
    #first[1] = ')' * right
    #return [first]
    return [['(' + ')' * right]]
  return_list = []
  for level in xrange(1, first[1] + 1):
    closed_first = RecursiveCalculate(left_copy, right - first[1])
    for item in closed_first:
      #return_list.append([first[0], ')'] + item)
      return_list.append(['(' + ')' * first[1]] + item)
  left_copy[0][1] = left_copy[0][1] + first[1]
  opened_first = RecursiveCalculate(left_copy, right)
  for item in opened_first:
    return_list.append(['('] + item)
    #return_list.append([[first[0], '']] + item)
  return return_list


def GetPairs(size):
  left = [['(', 1] for i in xrange(size / 2)]
  right = size / 2
  return RecursiveCalculate(left, right)

if __name__ == "__main__":
  for n in xrange(2, 24, 1):
    pairs = GetPairs(n * 2)
    print 'Valid combinations for %s pairs is: %s' % (n, len(pairs))
    #for pair in pairs:
    #  print ''.join(pair)
