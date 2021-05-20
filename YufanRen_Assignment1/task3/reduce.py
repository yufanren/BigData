#!/usr/bin/env python
import sys
import string

curr_key = None
total = 0
count = 0
for line in sys.stdin:
  key, value = line.strip().split('\t', 1)
  value = float(value)
  if key == curr_key:
    total += value
    count += 1
  else:
    if curr_key:
      avg = "{:.2f}".format(total / count)
      total = "{:.2f}".format(total)
      print '%s\t%s' % (curr_key, total + ', ' + avg)
    curr_key = key
    total = value
    count = 1
if curr_key:
  avg = "{:.2f}".format(total / count)
  total = "{:.2f}".format(total)
  print '%s\t%s' % (curr_key, total + ', ' + avg)