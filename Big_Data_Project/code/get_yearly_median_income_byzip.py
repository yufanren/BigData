import sys
import pandas as pd

START = 'Zip Code'
CATEGORY = 'All'
YEAR = 2019

#Get household income by each zip code region
#One Year only

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Requires 1 input file", file=sys.stderr)
    exit(-1)
  df = pd.read_csv(sys.argv[1])

  result = df.loc[(df['Location'].str.contains(START)) & (df['Household Type'].str.contains(CATEGORY))
                  & (df['TimeFrame'] == YEAR)].copy()
  result['Location'] = result['Location'].astype(str)
  result['ZipCode'] = result.apply(lambda x: x.Location.strip()[-5:], axis=1)
  result.drop('Location', axis=1, inplace=True)
  result.drop('Household Type', axis=1, inplace=True)
  result.drop('DataFormat', axis=1, inplace=True)
  result.drop('Fips', axis=1, inplace=True)
  result.columns = ['Year', 'Median_Household_Income', 'ZipCode']
  result[['ZipCode', 'Median_Household_Income', 'Year']].to_csv('../Median_Income_Byzip_2019.csv', index=False)
