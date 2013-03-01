#!/usr/bin/python
# Copyright 2011 Google Inc. All Rights Reserved.

"""
Example 'grep' for the C03 exercis for SRE-U 2011.

This implements all flags, and tries to match several idiosyncrasies of GNU
grep.

This is purposely not a good example of how to write code, but has a few nice
tricks in places.
"""

__author__ = 'bbrazil@google.com (Brian Brazil)'

import collections
import getopt
import itertools
import re
import sys
import os

class Args(object): pass


def ParseArgs(argv):
  args = Args()
  option_args = 'ABf'
  nonoption_args = 'ncwlLqrvxhHiFoz'
  for arg in nonoption_args:
    setattr(args, arg, False)

  args.A = 0
  args.B = 0
  args.f = False

  opts, remainder = getopt.getopt(
      argv[1:], nonoption_args + ''.join([x + ':' for x in option_args]))

  for o, v in opts:
    o = o[1:]
    if o not in option_args:
      v = True
    elif o in 'AB':
      v = int(v)
    setattr(args, o, v)
    if o == 'h':
      args.H = False
    elif o == 'H':
      args.h = False

    if o == 'l':
      args.L = False
    elif o == 'L':
      args.l = False

  if args.r:
    args.h = False
    args.H = True

  if args.L or args.l:
    args.c = False
    args.o = False

  if args.o:
    args.A = 0
    args.B = 0

  return args, remainder


def GenerateFiles(paths, args):
  if args.r:
    for p in paths:
      for root, _, files in os.walk(p):
        for f in files:
          fullpath = os.path.join(root, f)
          if os.path.isfile(fullpath):
            yield fullpath
  else:
    for f in paths:
      yield f


def AtLeastTwoFiles(filegen):
  first = None
  second = None
  try:
    first = filegen.next()
    second = filegen.next()
  except StopIteration:
    pass

  filegen = itertools.chain(
      [x for x in [first, second] if x is not None], filegen)
  return filegen, second is not None


def Match(line, patterns, args):
  if args.F:
    if args.i:
      line = line.lower()
    if args.x:
      matcher = lambda a, b: a == b
    else:
      matcher = lambda a, b: a in b
    for pattern in patterns:
      if matcher(pattern, line):
        if not args.v:
          return True, pattern
      else:
        if args.v:
          return True, None
  else:
    for pattern in patterns:
      match = pattern.search(line)
      if match:
        if not args.v:
          return True, match.group(0)
      else:
        if args.v:
          return True, None
  return False, None


def PrintLine(filename, line_no, text, context, args):
  if args.l or args.L or args.q or args.c:
    return
  output = []
  if args.H:
    output.append(filename)
  if args.n:
    output.append(str(line_no + 1))
  output.append(text)
  if context:
    sys.stdout.write('-'.join(output))
  else:
    sys.stdout.write(':'.join(output))


def GenLines(fd, args):
  if args.z:
    while True:
      line = ''
      buf = fd.read(8192)
      if not buf:
        if line:
          yield buf + '\0'
        return
      while True:
        pos = buf.find('\0')
        if pos == -1:
          line += buf
          break
        else:
          yield line + buf[:pos + 1]
          buf = buf[pos + 1:]
          line = ''
  else:
    for line in fd:
      if not line.endswith('\n'):
        line += '\n'
      yield line


def main(argv):
  args, argv = ParseArgs(argv)

  patterns = []
  if args.f:
    patterns.extend([p[:-1] for p in open(args.f)])
  else:
    patterns.append(argv.pop(0))

  if not argv:
    argv = ['-']

  filegen = GenerateFiles(argv, args)

  filegen, two_plus_files = AtLeastTwoFiles(filegen)
  if two_plus_files:
    if not args.h:
      args.h = False
      args.H = True
  else:
    if not args.H:
      args.h = True
      args.H = False

  if not args.F:
    if args.x:
      patterns = ["^(%s)$" % p for p in patterns]
    patterns = [re.compile(p, re.I if args.i else 0) for p in patterns]
  else:
    patterns = list(itertools.chain(*[p.split("\n") for p in patterns]))
    if args.i:
      patterns = [p.lower() for p in patterns]

  trailing = 0
  leading = collections.deque(maxlen=args.B)
  had_a_match = False

  for filename in filegen:
    if filename == '-':
      filename = '/dev/stdin'
    with open(filename, 'rb' if args.z else 'r') as f:
      lines_matched = 0
      for line_no, line in enumerate(GenLines(f, args)):
        if args.w:
          parts = re.split("[^\w_]+", line[:-1])
        else:
          parts = [line[:-1]]

        matches_found = []
        for part in parts:
          match, text = Match(part, patterns, args)
          if match:
            matches_found.append(text)
        if matches_found:
          lines_matched += 1
          if args.o:
            for mf in matches_found:
              PrintLine(filename, line_no, mf + '\n', False, args)
          else:
            if leading and not args.q and had_a_match:
              print '--'
            for ln, t in leading:
              PrintLine(filename, ln, t, True, args)
            leading.clear()
            PrintLine(filename, line_no, line, False, args)
          trailing = args.A
          had_a_match = True
        else:
          leading.append((line_no, line))
          if trailing:
            PrintLine(filename, line_no, line, True, args)
            trailing -= 1
    if not args.q:
      if args.l and lines_matched:
        print filename
      elif args.L and not lines_matched:
          print filename
      elif args.c:
        if args.H:
          print "%s:%s" % (filename, lines_matched)
        else:
          print lines_matched

  return 0 if had_a_match else 1


if __name__ == '__main__':
  os.sys.exit(main(sys.argv))
