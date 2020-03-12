import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 

# Reading in our data.
df = pd.read_csv('data/kc_house_data.csv')

def change_datetime(df, col):
	df[col] = df[col].apply(lambda x: x[:-7]).astype(int)
	df[col] = df[col].apply(lambda x: pd.to_datetime(x, format='%Y%m%d'))
	return df[col]

# A function that allows us to quickly view some bivariate 
# distributions.
def create_join_plot(df, col1, col2):
	sns.jointplot(x=col1, y=col2, data=df)
	plt.show()


def room_dist(df):

	# Setting our color palettes for our graphs
	sns.set_palette('Blues_d')
	sns.set_style('darkgrid')

	# Change date col from string to date time format.
	df['date'] = change_datetime(df, 'date')
	df = df[(df['sqft_lot15'] < 400000) & (df['bedrooms'] < 33)]

	# Building our color palette so we can use our color palette 
	# on barplots.
	pal = sns.color_palette('Blues_d', len(list(df['bedrooms'].unique())))
	pal1 = sns.color_palette('Blues_d', len(list(df['bathrooms'].unique())))

	# Barplot to look at how number of bedrooms impacts the price.
	fig1, ax = plt.subplots(nrows=3)
	sns.barplot(x='bedrooms', y='price', ci=None, data=df, ax=ax[0], palette=np.array(pal[::-1]))
	sns.barplot(x='bathrooms', y='price', ci=None, data=df, ax=ax[1], palette=np.array(pal1[::-1]))

	sns.distplot(a=df['bedrooms'], kde=False, color='b', ax=ax[2], hist_kws={'linewidth': 3})
	sns.distplot(a=df['bathrooms'], kde=False, color='g', ax=ax[2], hist_kws={'linewidth': 3})

	ax[0].set_xticks([i for i in range(12)])
	ax[2].set_xticks([i for i in range(11)])

	fig1.suptitle('Analysis by number of bedrooms/bathrooms in each house')
	fig1.show()

	plt.show()

if __name__ == '__main__':
	room_dist(df)