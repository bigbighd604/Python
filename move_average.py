#!/usr/bin/env python

import collections
import itertools


def GetMoveAverage2(l, n):
  it = iter(l)
  d = collections.deque(itertools.islice(it, n-1))
  d.appendleft(0)
  s = sum(d)
  for elem in it:
    s += elem - d.popleft()
    d.append(elem)
    yield s / float(n)


def GetMoveAverage(l, size):
  length = len(l)

  s = sum(l[:size])
  i = size

  while i < length:
    yield s / size
    s += l[i] - l[i - size]
    i += 1
  # last while iteration will cause i == length
  # But still need output the average number
  yield s / size

if __name__ == '__main__':
  l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
  results = GetMoveAverage(l, 4)
  for result in results:
    print result
  results = GetMoveAverage2(l, 4)
  for result in results:
    print result
