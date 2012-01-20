#!/usr/bin/env python

from functools import wraps

def memo(func):
  cache = {}
  @wraps(func)
  def wrap(*args):
    if args not in cache:
      cache[args] = func(*args)
    return cache[args]
  return wrap


# Recursive Solution
def rec_lcs(a, b):
  @memo
  def L(i, j):
    if min(i, j) < 0: return ''
    if a[i] == b[j]: return L(i - 1, j - 1) + a[i]
    return max(L(i - 1, j), L(i, j - 1))
  return L(len(a) - 1, len(b) - 1)


# Iterative Solution
def lcs_iter(a, b):
  n, m = len(a), len(b)
  pre, cur = [0] * (n + 1), [0] * (n + 1)
  for j in range(1, m + 1):
    pre, cur = cur, pre
    for i in range(1, n + 1):
      if a[i-1] == b[j-1]:
        cur[i] = pre[i-1] + 1
      else:
        cur[i] = max(pre[i], cur[i-1])
  return cur[n]


if __name__ == '__main__':
  str1 = 'abcdefg'
  str2 = 'xybhebg'
  print str1, str2, rec_lcs(str1, str2), lcs_iter(str1, str2)
  str1 = 'Starwalker'
  str2 = 'Starbuck'
  print str1, str2, rec_lcs(str1, str2), lcs_iter(str1, str2)
