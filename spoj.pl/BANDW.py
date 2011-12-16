#!/usr/bin/env python


def calculate(source, target):
  counter = 0
  flag = False
  for i, c in enumerate(source):
    if c != target[i]:
      if not flag:
        flag = True
        counter += 1
    elif flag:
        flag = False

  return counter


if __name__ == '__main__':
  while True:
    s, t = (raw_input()).split()
    if s != '*':
      print calculate(s, t)
    else:
      break
