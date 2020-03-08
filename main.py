import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
df = pd.read_csv('data/kc_house_data.csv')

def change_datetime(df, col):
	for index, row in df.iterrows():
		df.loc[index, col] = df.loc[index, col].replace('T', '')
		df.loc[index, col] = df.loc[index, col][:-6]

	df[col]= df[col].astype(int)
	df[col] = df[col].apply(lambda x: pd.to_datetime(x, format='%Y%m%d'))
	return df[col]


print(df.head())

print(df.dtypes)

print(df['date'])

# Change date col from string to date time format.
df['date'] = change_datetime(df, 'date')

print(df['date'])

fig2, ax = plt.subplots(nrows=1)

sns.scatterplot(x='date', y='price', data=df, ax=ax)
plt.xlim(pd.to_datetime('2014-05-01'),pd.to_datetime('2015-05-01'))
plt.show()