#!/usr/bin/env python
import sys
import string

def QuotationFix(s):
  new_s, i = [], 0
  while i < len(s):
    if '"' in s[i]:
      item = s[i]
      counter = i
      i += 1
      while counter < len(s) - 1 and '"' not in s[counter + 1]:
        counter += 1
      for j in range (i, min(counter + 2, len(s))):
        item += ',' + s[j]
      new_s.append(item.replace('"', ''))
      i = counter + 1
    else:
      new_s.append(s[i])
    i += 1
  return new_s

weekend = {'05', '06', '12', '13', '19', '20', '26', '27'}
violation_count = {}

#place violation_code and counts into dictionary
#code as key and weekday count in value[0], weekend count in value[1]
for line in sys.stdin:
  info = line.strip().split(',')
  if '"' in line:
    info = QuotationFix(info)
  date = info[1].strip().split('-')[2]
  code = info[2]
  if len(info) != 22 or info[0] == 'summons_number':
    continue
  if code in violation_count:
    violation_count[code][0 if date in weekend else 1] += 1
  else:
    counts = [0, 0]
    counts[0 if date in weekend else 1] += 1
    violation_count[code] = counts
for key, value in violation_count.items():
  value = str(value[0]) + '\t' + str(value[1])
  print '%s\t%s' % (key, value)

