#!/usr/bin/env python
import sys
import string

curr_key = None
curr_count = 0
curr_max = 0
key_max = None
for line in sys.stdin:
  key, value = line.strip().split('\t', 1)
  if key == curr_key:
    curr_count += int(value)
  else:
    if curr_count > curr_max:
      key_max = curr_key
      curr_max = curr_count
    curr_key = key
    curr_count = int(value)
if curr_count > curr_max:
  key_max = curr_key
  curr_max = curr_count
if curr_key:
  print '%s\t%d' % (key_max, curr_max)