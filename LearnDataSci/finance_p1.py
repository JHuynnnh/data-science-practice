'''
Python For Finance, Part 1

Modified script from:
http://www.learndatasci.com/python-finance-part-yahoo-finance-api-pandas-matplotlib/

Used google finance instead of yahoo finance, since I was having issues with yahoo finance.

'''

from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
from pprint import pprint

# select stocks traded on the NASDAQ
tickers = ['AAPL', 'MSFT', 'YHOO', 'FB']

# Define which online source one should use
data_source = 'google'

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2000-01-01'
end_date = '2016-12-31'

# load data
panel_data = data.DataReader(tickers, data_source, start_date, end_date)

# get DataFrame of closing prices
close = panel_data.ix['Close']

# Getting all weekdays between 01/01/2000 and 12/31/2016
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

# align closing prices with new date index and fill NaNs 
# (note: method='ffil' did not work as expected)
close = close.reindex(all_weekdays)
close = close.fillna(method='bfill')

print(close.describe())

# print time series data
fig_count = 0
for ticker in tickers:
	tick = close.ix[:, ticker]

	# Calculate the 20 and 100 days moving averages of the closing prices
	short_rolling = tick.rolling(window=20).mean()
	long_rolling = tick.rolling(window=100).mean()

	# Plot everything by leveraging the very powerful matplotlib package
	fig = plt.figure(fig_count)
	ax = fig.add_subplot(1,1,1)
	ax.plot(tick.index, tick, label=ticker)
	ax.plot(short_rolling.index, short_rolling, label='20 days rolling')
	ax.plot(long_rolling.index, long_rolling, label='100 days rolling')
	ax.set_xlabel('Date')
	ax.set_ylabel('Closing price ($)')
	ax.legend()
	fig_count += 1

plt.show()





