import sys
import numpy as np
import pandas as pd

#Get latitude and longitude form incidents data
#This table conforms to Texas A&M geoservices' bulk request format

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Requires 1 input file", file=sys.stderr)
    exit(-1)
  df = pd.read_csv(sys.argv[1])
  df['row'] = np.arange(len(df))
  df1 = df.apply(lambda x: [x[19], x[16], x[17], 'NY'], axis=1, result_type='expand')
  df1.columns = ['ID', 'Latitude_y', 'Longitude_y', 'State']
  df1.to_csv('../2006-19_NYC_Shooting_Incident.csv', index=False)

