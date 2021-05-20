#!/usr/bin/env python
import sys
import string

p = "summons_number,issue_date,violation_code,violation_county,violation_description,violation_location,violation_precinct,violation_time,time_first_observed,meter_number,issuer_code,issuer_command,issuer_precinct,issuing_agency,plate_id,plate_type,registration_state,street_name,vehicle_body_type,vehicle_color,vehicle_make,vehicle_year"
p = p.split(',')

park_data_index = [p.index('plate_id'), p.index('violation_precinct'),p.index('violation_code'),p.index('issue_date')]

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

# split the lines into a pair
for line in sys.stdin:
	info = line.strip().split(',')
	if '"' in line:
		info = QuotationFix(info)
	if info[0] == 'summons_number':
		continue
	key = info[0]
	if len(info) == 22:
		values = list(info[i] for i in park_data_index)
		print '%s\t%s' % (key, ', '.join(values))
	elif len(info) == 18:
		print(key + '\t')




