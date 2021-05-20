#!/usr/bin/env python
import sys
import string

curr_key = None
total_count = 0
for line in sys.stdin:
  key, value = line.strip('\n').split('\t', 1)
  if isinstance(value, str):
    value = int(value)
  if key == curr_key:
    total_count += value
  else:
    if curr_key:
      print '%s\t%d' % (curr_key, total_count)
    curr_key = key
    total_count = value
if curr_key:
  print '%s\t%d' % (curr_key, total_count)
