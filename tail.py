#!/usr/bin/env python

import collections
import os
import sys

BUF_SIZE = 4096

def Tail(file, num_lines = 10):
  with open(file) as f:
    lines_already_found = 0
    buffer_size = BUF_SIZE
    file_length = os.stat(file).st_size
    remain_length = file_length

    while remain_length:
      if buffer_size < remain_length:
        remain_length -= buffer_size
      else:
        buffer_size = remain_length
        remain_length = 0

      f.seek(remain_length)
      data = f.read(buffer_size)
      i = buffer_size
      while lines_already_found <= num_lines:
        i -= 1
        if i < 0:
          break
        if data[i] == '\n':
          lines_already_found += 1
      if lines_already_found == num_lines + 1:
        break

    f.seek(remain_length + i + 1)
    while True:
      data = f.read(BUF_SIZE)
      if data:
        sys.stdout.write(data)
      else:
        break

"""Comments in master"""
"""This is comments in experimental."""

def Tail2(file, num_lines= 10):
  with open(file) as f:
    d = collections.deque(f, 10)
  for item in d:
    sys.stdout.write(item)

if __name__ == '__main__':
  Tail2(sys.argv[1])
