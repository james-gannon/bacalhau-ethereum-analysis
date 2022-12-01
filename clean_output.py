# Use pandas to read in transation data and clean up the columns
import pandas as pd
import glob

file = glob.glob(
    'output_*/transactions/start_block=*/end_block=*/transactions*.csv')[0]
print("Loading file %s" % file)
df = pd.read_csv(file)
df['value'] = df['value'].astype('float')
df['from_address'] = df['from_address'].astype('string')
df['to_address'] = df['to_address'].astype('string')
df['hash'] = df['hash'].astype('string')
df['block_hash'] = df['block_hash'].astype('string')
df['block_datetime'] = pd.to_datetime(df['block_timestamp'], unit='s')
df.info()


# Total volume per day
df[['block_datetime', 'value']].groupby(
    pd.Grouper(key='block_datetime', freq='1D')).sum().plot()
