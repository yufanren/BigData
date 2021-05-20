#!/usr/bin/env python
import sys
import string

curr_key = None
curr_value = []
value_ready = False
for line in sys.stdin:
	key, value = line.strip('\n').split('\t', 1)
	if key != curr_key:
		if value_ready:
			for v in curr_value:
				print '%s\t%s' % (curr_key, v)
			value_ready = False
		curr_key = key
		if value:
			curr_value = [value]
			value_ready = True
		else:
			curr_value = []
	else:
		if value:
			curr_value.append(value)
		else:
			value_ready = False
if value_ready:
	for v in curr_value:
		print '%s\t%s' % (curr_key, v)
