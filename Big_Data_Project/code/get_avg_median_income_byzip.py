import sys
import pandas as pd

START = 'Zip Code'
CATEGORY = 'All'

#get 3 year average household income from median income.csv
#only includes the zip code section

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Requires 1 input file", file=sys.stderr)
    exit(-1)
  df = pd.read_csv(sys.argv[1])

  result = df.loc[(df['Location'].str.contains(START)) & (df['Household Type'].str.contains(CATEGORY))].copy()

  result['Location'] = result['Location'].astype(str)
  result['ZipCode'] = result.apply(lambda x: x.Location.strip()[-5:], axis=1)
  result.drop('Location', axis=1, inplace=True)
  result.drop('Household Type', axis=1, inplace=True)
  result.drop('DataFormat', axis=1, inplace=True)
  result.drop('Fips', axis=1, inplace=True)
  result.drop('TimeFrame', axis=1, inplace=True)
  result.columns = ['Median_Household_Income', 'ZipCode']
  result2 = result[['ZipCode', 'Median_Household_Income']].copy()
  result2['Median_Household_Income'] = pd.to_numeric(result2['Median_Household_Income'], downcast="float")
  result2.groupby('ZipCode').agg('mean').reset_index().to_csv('../Median_Income_Byzip_Avg.csv', index=False)