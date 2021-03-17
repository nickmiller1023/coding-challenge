import pandas as pd

dataset_url = 'https://data.ny.gov/api/views/3x8r-34rs/rows.csv?accessType=DOWNLOAD'
solar = pd.read_csv(dataset_url, sep=',')

#solar = pd.read_csv('C:/Users/millnd/Desktop/Solar_Electric_Programs_Reported_by_NYSERDA__Beginning_2000.csv')

column_list = list(solar)

#print each column name in sorted order
column_list.sort()
print(column_list)
print()

#print total number of rows in data frame
rows = len(solar)
print('There are ' + str(rows) + ' rows in the dataset')

#Create new column 'Total Cost' by subtracting '$Incentive' from 'Project Cost'
#Start by filling in blank cells with zeroes
solar['Project Cost'] = solar['Project Cost'].fillna(0)
solar['$Incentive'] = solar['$Incentive'].fillna(0)
solar['Total Cost'] = solar['Project Cost'] - solar['$Incentive']
solar.to_csv('Solar.csv', index = False) 
