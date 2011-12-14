#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# string search algorithm KMP
# It use failure function to determine steps to fallback
# http://en.wikipedia.org/wiki/Knuth–Morris–Pratt_algorithm
#


def BuildFailureFunction(needle):
  length = len(needle)
  failure_table = [0 for i in xrange(length)]
  failure_table[0] = -1
  position = 2
  index = 0
  while position < length:
    # first case: the substring continues
    if needle[position - 1] == needle[index]:
      index += 1
      failure_table[position] = index
      position += 1
    # second case: it doesn't but we can fall back
    elif index > 0:
      index = failure_table[index]
    # third case: we have run out of candiates. index = 0
    else:
      failure_table[position] = 0
      position += 1
  return failure_table


def KMPSearch(haystack, needle):
  haystack_length = len(haystack)
  needle_length = len(needle)
  failure_table = BuildFailureFunction(needle)

  m = 0 # the beginning of the current match in haystack
  i = 0 # the position of the current character in needle

  while m + i < haystack_length:
    if needle[i] == haystack[m + i]:
      if i == needle_length - 1:
        return m
      i += 1
    else:
      m = m + i - failure_table[i]
      if failure_table[i] > -1:
        i = failure_table[i]
      else:
        i = 0
      print 'Jump to %s, set i to %s' % (m, i)
  return -1


if __name__ == "__main__":
  print BuildFailureFunction("ABABABCABABD")
  print BuildFailureFunction("AAAAAAAD")
  print BuildFailureFunction("ABCDEABCDEFABCDED")
  needle = "ABCDABD"
  haystack = "ABC ABCDAB ABCDABCDABDE"
  print 'needle: %s' % needle
  print 'failure function: %s' % BuildFailureFunction(needle)
  print 'haystack: %s' % haystack
  print 'Match position: %s' % KMPSearch(haystack, needle)
  needle = "PARTICIPATE IN PARACHUTE"
  print BuildFailureFunction(needle)
