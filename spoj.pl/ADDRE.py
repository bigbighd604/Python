#!/usr/bin/env python

num_map = {
    '0':0, '1':1, '2':2, '3':3, '4':4
    '5':5, '6':6, '7':7, '8':8, '9':9
    }


if __name__ == '__main__':
  lines = int(raw_input())
  for i in xrange(lines):
    n1, n2 = raw_input().split()
    n1 = n1[::-1]
    n2 = n2[::-1]
    n3 = int(n1) + int(n2)
    print str(n3)[::-1].strip('0')
