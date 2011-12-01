#!/usr/bin/env python

import sys

def find_dup_id(path):
  dup_id = {}
  f = open(path, 'r')
  for line in f.readlines():
    user, pwd, uid = line.split(':')[0:3]
    if uid not in dup_id:
      dup_id[uid] = [user]
    else:
      dup_id[uid].append(user)

  for uid, users in dup_id.iteritems():
    if len(users) > 1:
      print uid, users


if __name__ == '__main__':
  find_dup_id(sys.argv[1])
