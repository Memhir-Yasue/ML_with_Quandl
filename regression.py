import pandas as pandas
import quandl

my_data = quandl.get('WIKI/GOOGL')

my_data = my_data[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

# Measuring volatility
# Creating new features (HighLow_PCT PCT_change)

my_data['HighLow_PCT'] = (my_data['Adj. High'] - my_data['Adj. Close']) / my_data['Adj. Close'] * 100.0
my_data['PCT_change'] = (my_data['Adj. Close'] - my_data['Adj. Open']) / my_data['Adj. Open'] * 100.0

# Columns/features we care about

# Features we care about
my_data = my_data[['Adj. Close', 'HighLow_PCT', 'PCT_change', 'Adj. Volume']]

print(my_data.head())