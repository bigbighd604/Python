#!/usr/bin/env python
#
# Q. Given a list of numbers, find out longest increasing sequence
# Requirements:
# 1. Time complexity - O(n)
#
# i.e.
# input: 1 4 2 3 7 5 6 should give: 1 2 3 5 6
#


import bisect
import random
import sys


# This function returns the length of longest increasing sequence.
def lis(seq):
  end = []
  for v in seq:
    idx = bisect.bisect(end, v)
    if idx == len(end): end.append(val)
    else: end[idx] = v
  return len(end)


def GenerateList(size):
  return [random.randint(1, 500) for i in xrange(size)]


def LongestSequence(numbers):
  length = len(numbers)
  result = [[] for i in xrange(length)]
  result[0].append(numbers[0])

  for i in xrange(1, length):
    i_length = len(result[i])
    temp_list = []
    for j in xrange(i):
      if numbers[j] < numbers[i] and len(result[j]) > i_length:
        temp_list = result[j]
        # update i_length only got longer sequences
        i_length = len(result[j])

    result[i].extend(temp_list)
    result[i].append(numbers[i])

#  return result
  sequences = [result[0]]
  for sequence in result:
    if len(sequence) > len(sequences[0]):
      sequences = [sequence]
    elif len(sequence) == len(sequences[0]):
      sequences.append(sequence)
  return sequences


if __name__ == "__main__":
  numbers1 = [1,4,2,3,7,5,6,8,5,9,11,10,12]
  numbers2 = [20,18,22,26,22,24,30,25,32,26,1,3,2,4,2,5,7,6,8,9,10]
  size = int(sys.argv[1])
  l = GenerateList(size)
  print l
  results = LongestSequence(l)
  for line in results:
    print line
  n3=[180, 359, 226, 434, 251, 116, 33, 97, 366, 169, 289, 193, 120, 215, 281, 452, 247, 6, 230, 107]
  results = LongestSequence(n3)
  for line in results:
    print line
