import logging
import sys
import csv
from time import sleep
from random import randint
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

START = 0

#Get zip code from latitude and longitude
#start with row no. START
#first column is index number
user_agent = 'user_id_{}'.format(randint(10000,99999))
geocoder = Nominatim(user_agent = user_agent)

def get_zipcode(geocoder, lat, long, sleep_sec):
  try:
    return geocoder.reverse((lat, long), language='en', exactly_one=True).raw['address']['postcode']
  except GeocoderTimedOut:
      logging.info('TIMED OUT: GeocoderTimedOut: Retrying...')
      sleep(randint(1*100,sleep_sec*100)/100)
      return get_zipcode(geocoder, lat, long, randint(1, 3))
  except GeocoderServiceError as e:
      logging.info('CONNECTION REFUSED: GeocoderServiceError encountered.')
      logging.error(e)
      return get_zipcode(geocoder, lat, long, randint(1, 3))
  except (AttributeError, KeyError, ValueError):
      return 'Error'

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Requires 1 input file", file=sys.stderr)
    exit(-1)

  if START == 0:
    print("index,Latitude,Longitude,Zipcode")
  with open(sys.argv[1], 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      if int(row[0]) < START:
        continue
      sleep(randint(1 * 100, randint(1, 2) * 100) / 100)
      row.append(get_zipcode(geocoder, row[1], row[2], randint(1, 3)))
      print(','.join(row))


