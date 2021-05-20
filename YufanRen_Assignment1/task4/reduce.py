#!/usr/bin/env python
import sys
import string

ny_count = 0
other_count = 0
for line in sys.stdin:
  key, value = line.strip().split('\t', 1)
  if key == 'NY':
    ny_count += int(value)
  else:
    other_count += int(value)
if ny_count:
  print '%s\t%d' % ('NY', ny_count)
if other_count:
  print '%s\t%d' % ('Other', other_count)