import sys
import pandas as pd
import numpy as np
import re

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Requires 1 input file", file=sys.stderr)
    exit(-1)

  df_incident = pd.read_csv(sys.argv[1])
  df_incident['row'] = np.arange(len(df_incident))

  df_zipcode = pd.read_csv(sys.argv[2])
  df_zipcode['ZipCode'] = df_zipcode.apply(lambda x: re.split('-|:', str(x.Zipcode).strip())[0], axis=1)

  df = pd.merge(left=df_incident, right=df_zipcode, left_on='row', right_on='index')
  df.drop('row', axis=1, inplace=True)
  df.drop('index', axis=1, inplace=True)
  df.drop('Latitude_y', axis=1, inplace=True)
  df.drop('Longitude_y', axis=1, inplace=True)
  df.drop('Zipcode', axis=1, inplace=True)

  df.to_csv('../2020_incident_with_zipcode.csv', index=False)



