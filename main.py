import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 


sns.set_palette('Blues_d')
sns.set_style('darkgrid')

df = pd.read_csv('data/kc_house_data.csv')

def change_datetime(df, col):
	df[col] = df[col].apply(lambda x: x[:-7]).astype(int)
	df[col] = df[col].apply(lambda x: pd.to_datetime(x, format='%Y%m%d'))
	return df[col]


# Change date col from string to date time format.
df['date'] = change_datetime(df, 'date')

df = df[df['sqft_lot15'] < 400000]

pal=sns.color_palette('Blues_d', len(list(df['bedrooms'].unique())))

# Barplot fig 1
fig1, ax = plt.subplots(nrows=1)
sns.barplot(x='bedrooms', y='price', ci=None, data=df, palette=np.array(pal[::-1]))
fig1.show()

# scatter plot fig 2
fig2, ax = plt.subplots(nrows=1)
sns.scatterplot(x='sqft_living15', y='price', data=df, ax=ax)
fig2.show()

# scatter plot fig 3
fig3, ax = plt.subplots(nrows=1)
sns.scatterplot(x='sqft_lot15', y='price', data=df, ax=ax)
plt.show()

input('Press Enter to Stop...')