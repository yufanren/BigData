#!/usr/bin/env python
import sys
import string

curr_key = None
curr_count = 0

for line in sys.stdin:
  key, value = line.strip().split('\t', 1)
  if key == curr_key:
    curr_count += int(value)
  else:
    if isinstance(curr_key, str):
      column, term = curr_key.split(',', 1)
      if column == 'b':
        column = 'vehicle_color'
      elif column == 'a':
        column = 'vehicle_make'
      print '%s\t%s' % (column, term + ', ' + str(curr_count))
    curr_key = key
    curr_count = int(value)
if isinstance(curr_key, str):
  column, term = curr_key.split(',', 1)
  if column == 'b':
    column = 'vehicle_color'
  elif column == 'a':
    column = 'vehicle_make'
  print '%s\t%s' % (column, term + ', ' + str(curr_count))




