#!/usr/bin/env python
import sys
import string

curr_key = None
curr_weekday_count = 0
curr_weekend_count = 0

for line in sys.stdin:
  key, weekend, weekday = line.strip().split('\t', 2)
  weekday_counts = float(weekday)
  weekend_counts = float(weekend)
  if key == curr_key:
    curr_weekday_count += weekday_counts
    curr_weekend_count += weekend_counts
  else:
    if curr_key:
      value = "{:.2f}".format(curr_weekend_count / 8) + ', ' + "{:.2f}".format(curr_weekday_count / 23)
      print '%s\t%s' % (curr_key, value)
    curr_key = key
    curr_weekday_count = weekday_counts
    curr_weekend_count = weekend_counts
if curr_key:
  value = "{:.2f}".format(curr_weekend_count / 8) + ', ' + "{:.2f}".format(curr_weekday_count / 23)
  print '%s\t%s' % (curr_key, value)
