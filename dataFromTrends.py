
## 429 blocked by Google

from pytrends.request import TrendReq
 # hl=host language, tz=time zone
pytrends = TrendReq(hl='en-US', tz=360, timeout=(10,25), proxies=['https://34.203.233.13:80',], retries=2, backoff_factor=0.1, requests_args={'verify':False})
# setting
kw_list = ['chatgpt'] 
pytrends.build_payload(kw_list, cat=0, 
						timeframe='2022-12-01 2023-01-01', 
                        geo='KR', gprop='')
df = pytrends.interest_over_time()

print(df)