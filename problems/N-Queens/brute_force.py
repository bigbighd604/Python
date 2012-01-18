#!/usr/bin/python
#
# http://en.wikipedia.org/wiki/Eight_queens_puzzle
#

from itertools import permutations

n = 8
cols = range(n)
results = []

for vec in permutations(cols):
  # check diagonal attack, for col position, m and n:
  # abs(vec[m] - vec[n]) == abs(m - n) if there is diagonal attack
  # means:
  # a. vec[m] - vec[n] = m - n ==> vec[m] - m == vec[n] - n
  # b. vec[m] - vec[n] = n - m ==> vec[m] + m == vec[n] + n
  # if exists one pair (m, n), then there is diagonal attack.
  if (n == len(set(vec[i]+i for i in cols)) ==
      len(set(vec[i]-i for i in cols))):
    results.append(vec)


print results
