import pyupbit

ticker = 'BTC'
interval = 'day'
rows = 100
currentPath = "C:\\Users\\mysel\\Dev\\Github\\crypto-forcasting\\"

tickers = pyupbit.get_tickers('KRW')  # Tickers on KRW

major_tickers = [ 'BTC','ETH','XRP','DOGE' ]

intervals = ['day', 'minute1', 'minute3', 'minute5', 'minute10', 'minute15',
             'minute30', 'minute60', 'minute240', 'week', 'month']

columns = ['open', 'high', 'low', 'close', 'volume', 'value']


#df = pyupbit.get_ohlcv('KRW-BTC')
df = pyupbit.get_ohlcv(ticker=('KRW-'+ticker), interval=interval, count=rows, to=None, period=1)
print(df.tail())

df.to_csv(currentPath + ticker+'_'+interval+'.csv')
