#!/usr/bin/env python


def ReBalance(alist, i):
  length = len(alist)
  index = i
  if (2 * i) < length and alist[i] < alist[2 * i]:
    index = 2 * i
  if (2* i + 1) < length and alist[index] < alist[2 * i + 1]:
    index = index + 1
  if index != i:
    alist[i], alist[index] = alist[index], alist[i]
    ReBalance(alist, index)


def GetHeap(alist):
  length = len(alist)
  start = length / 2 - 1

  for i in range(start, 0, -1):
    ReBalance(alist, i)
  return alist


if __name__ == '__main__':
  alist = [5, 13, 2, 25, 7, 17, 20, 8, 4]
  print GetHeap(alist)
