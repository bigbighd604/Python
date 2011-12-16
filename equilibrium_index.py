#!/usr/bin/env python


def GetEquilibriumIndex(l):
  s = sum(l)
  ls = 0
  results = []
  for i in xrange(len(l)):
    s -= l[i]
    if ls == s:
      results.append(i)
    ls += l[i]

  return results

if __name__ == '__main__':
  l = [-7, 1, 5, 2, -4, 3, 0]
  results = GetEquilibriumIndex(l)
  for result in results:
    print result
