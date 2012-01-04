#!/usr/bin/env python
#
# Can extend to unique words, duplicate words etc.
#

import sys

def IsUnique(string):
  d = {}
  for char in string:
    if char in d:
      return False
    else:
      d[char] = True
  return True

if __name__ == '__main__':
  string = sys.argv[1]
  if IsUnique(string):
    print 'Is Unique!'
  else:
    print 'Not Unique!'
