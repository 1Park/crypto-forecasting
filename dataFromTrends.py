from serpapi import GoogleSearch
import csv

def export_to_csv(data, filename='output.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        
        fieldnames = ['date', 'timestamp', 'query', 'value', 'extracted_value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        if 'interest_over_time' in data and 'timeline_data' in data['interest_over_time']:
            for item in data['interest_over_time']['timeline_data']:
                row_data = {}
                row_data['date'] = item['date']
                row_data['timestamp'] = item['timestamp']
                # Accessing the first element in 'values' list (only one value per date)
                row_data['query'] = item['values'][0]['query']
                row_data['value'] = item['values'][0]['value']
                row_data['extracted_value'] = item['values'][0]['extracted_value']
                writer.writerow(row_data)


key_path = 'serpKey.txt' # Your SERP API key is saved in this path
with open(key_path, 'r') as file:
    key = file.read()

params = {
  "api_key": key,
  "engine": "google_trends",
  "q": "BTC",
  "geo": "KR",
  "tz": "-540",
  "date": "2021-01-01 2021-03-01"
}

filename = params["engine"] + "_" +params["q"] +"_"+ params["geo"] +"_" + params["date"].replace(" ","_") + ".csv"


#result_example = {'search_metadata': {'id': '-----', 'status': 'Success', 'json_endpoint': '------', 'created_at': '2024-11-21 12:24:23 UTC', 'processed_at': '2024-11-21 12:24:23 UTC', 'google_trends_url': 'https://trends.google.com/trends/api/explore?hl=en&tz=30&req=%7B%22comparisonItem%22%3A%5B%7B%22keyword%22%3A%22BTC%22%2C%22geo%22%3A%22KR%22%2C%22time%22%3A%222021-01-01+2021-03-01%22%7D%5D%2C%22category%22%3A0%2C%22property%22%3A%22%22%2C%22userConfig%22%3A%22%7BuserType%3A+%5C%22USER_TYPE_LEGIT_USER%5C%22%7D%22%7D', 'raw_html_file': 'https://serpapi.com/searches/98e27bb3fa08012c/673f2677dc969f4c282f208b.html', 'prettify_html_file': 'https://serpapi.com/searches/98e27bb3fa08012c/673f2677dc969f4c282f208b.prettify', 'total_time_taken': 21.14}, 'search_parameters': {'engine': 'google_trends', 'q': 'BTC', 'hl': 'en', 'geo': 'KR', 'date': '2021-01-01 2021-03-01', 'tz': '30', 'data_type': 'TIMESERIES'}, 'interest_over_time': {'timeline_data': [{'date': 'Jan 1, 2021', 'timestamp': '1609459200', 'values': [{'query': 'BTC', 'value': '34', 'extracted_value': 34}]}, {'date': 'Jan 2, 2021', 'timestamp': '1609545600', 'values': [{'query': 'BTC', 'value': '41', 'extracted_value': 41}]}, {'date': 'Jan 3, 2021', 'timestamp': '1609632000', 'values': [{'query': 'BTC', 'value': '74', 'extracted_value': 74}]}, {'date': 'Jan 4, 2021', 'timestamp': '1609718400', 'values': [{'query': 'BTC', 'value': '52', 'extracted_value': 52}]}, {'date': 'Jan 5, 2021', 'timestamp': '1609804800', 'values': [{'query': 'BTC', 'value': '29', 'extracted_value': 29}]}, {'date': 'Jan 6, 2021', 'timestamp': '1609891200', 'values': [{'query': 'BTC', 'value': '41', 'extracted_value': 41}]}, {'date': 'Jan 7, 2021', 'timestamp': '1609977600', 'values': [{'query': 'BTC', 'value': '50', 'extracted_value': 50}]}, {'date': 'Jan 8, 2021', 'timestamp': '1610064000', 'values': [{'query': 'BTC', 'value': '69', 'extracted_value': 69}]}, {'date': 'Jan 9, 2021', 'timestamp': '1610150400', 'values': [{'query': 'BTC', 'value': '60', 'extracted_value': 60}]}, {'date': 'Jan 10, 2021', 'timestamp': '1610236800', 'values': [{'query': 'BTC', 'value': '54', 'extracted_value': 54}]}, {'date': 'Jan 11, 2021', 'timestamp': '1610323200', 'values': [{'query': 'BTC', 'value': '79', 'extracted_value': 79}]}, {'date': 'Jan 12, 2021', 'timestamp': '1610409600', 'values': [{'query': 'BTC', 'value': '55', 'extracted_value': 55}]}, {'date': 'Jan 13, 2021', 'timestamp': '1610496000', 'values': [{'query': 'BTC', 'value': '44', 'extracted_value': 44}]}, {'date': 'Jan 14, 2021', 'timestamp': '1610582400', 'values': [{'query': 'BTC', 'value': '58', 'extracted_value': 58}]}, {'date': 'Jan 15, 2021', 'timestamp': '1610668800', 'values': [{'query': 'BTC', 'value': '46', 'extracted_value': 46}]}, {'date': 'Jan 16, 2021', 'timestamp': '1610755200', 'values': [{'query': 'BTC', 'value': '39', 'extracted_value': 39}]}, {'date': 'Jan 17, 2021', 'timestamp': '1610841600', 'values': [{'query': 'BTC', 'value': '38', 'extracted_value': 38}]}, {'date': 'Jan 18, 2021', 'timestamp': '1610928000', 'values': [{'query': 'BTC', 'value': '44', 'extracted_value': 44}]}, {'date': 'Jan 19, 2021', 'timestamp': '1611014400', 'values': [{'query': 'BTC', 'value': '29', 'extracted_value': 29}]}, {'date': 'Jan 20, 2021', 'timestamp': '1611100800', 'values': [{'query': 'BTC', 'value': '35', 'extracted_value': 35}]}, {'date': 'Jan 21, 2021', 'timestamp': '1611187200', 'values': [{'query': 'BTC', 'value': '60', 'extracted_value': 60}]}, {'date': 'Jan 22, 2021', 'timestamp': '1611273600', 'values': [{'query': 'BTC', 'value': '54', 'extracted_value': 54}]}, {'date': 'Jan 23, 2021', 'timestamp': '1611360000', 'values': [{'query': 'BTC', 'value': '33', 'extracted_value': 33}]}, {'date': 'Jan 24, 2021', 'timestamp': '1611446400', 'values': [{'query': 'BTC', 'value': '40', 'extracted_value': 40}]}, {'date': 'Jan 25, 2021', 'timestamp': '1611532800', 'values': [{'query': 'BTC', 'value': '36', 'extracted_value': 36}]}, {'date': 'Jan 26, 2021', 'timestamp': '1611619200', 'values': [{'query': 'BTC', 'value': '42', 'extracted_value': 42}]}, {'date': 'Jan 27, 2021', 'timestamp': '1611705600', 'values': [{'query': 'BTC', 'value': '47', 'extracted_value': 47}]}, {'date': 'Jan 28, 2021', 'timestamp': '1611792000', 'values': [{'query': 'BTC', 'value': '26', 'extracted_value': 26}]}, {'date': 'Jan 29, 2021', 'timestamp': '1611878400', 'values': [{'query': 'BTC', 'value': '43', 'extracted_value': 43}]}, {'date': 'Jan 30, 2021', 'timestamp': '1611964800', 'values': [{'query': 'BTC', 'value': '42', 'extracted_value': 42}]}, {'date': 'Jan 31, 2021', 'timestamp': '1612051200', 'values': [{'query': 'BTC', 'value': '47', 'extracted_value': 47}]}, {'date': 'Feb 1, 2021', 'timestamp': '1612137600', 'values': [{'query': 'BTC', 'value': '38', 'extracted_value': 38}]}, {'date': 'Feb 2, 2021', 'timestamp': '1612224000', 'values': [{'query': 'BTC', 'value': '26', 'extracted_value': 26}]}, {'date': 'Feb 3, 2021', 'timestamp': '1612310400', 'values': [{'query': 'BTC', 'value': '34', 'extracted_value': 34}]}, {'date': 'Feb 4, 2021', 'timestamp': '1612396800', 'values': [{'query': 'BTC', 'value': '33', 'extracted_value': 33}]}, {'date': 'Feb 5, 2021', 'timestamp': '1612483200', 'values': [{'query': 'BTC', 'value': '29', 'extracted_value': 29}]}, {'date': 'Feb 6, 2021', 'timestamp': '1612569600', 'values': [{'query': 'BTC', 'value': '44', 'extracted_value': 44}]}, {'date': 'Feb 7, 2021', 'timestamp': '1612656000', 'values': [{'query': 'BTC', 'value': '46', 'extracted_value': 46}]}, {'date': 'Feb 8, 2021', 'timestamp': '1612742400', 'values': [{'query': 'BTC', 'value': '51', 'extracted_value': 51}]}, {'date': 'Feb 9, 2021', 'timestamp': '1612828800', 'values': [{'query': 'BTC', 'value': '100', 'extracted_value': 100}]}, {'date': 'Feb 10, 2021', 'timestamp': '1612915200', 'values': [{'query': 'BTC', 'value': '45', 'extracted_value': 45}]}, {'date': 'Feb 11, 2021', 'timestamp': '1613001600', 'values': [{'query': 'BTC', 'value': '62', 'extracted_value': 62}]}, {'date': 'Feb 12, 2021', 'timestamp': '1613088000', 'values': [{'query': 'BTC', 'value': '82', 'extracted_value': 82}]}, {'date': 'Feb 13, 2021', 'timestamp': '1613174400', 'values': [{'query': 'BTC', 'value': '59', 'extracted_value': 59}]}, {'date': 'Feb 14, 2021', 'timestamp': '1613260800', 'values': [{'query': 'BTC', 'value': '59', 'extracted_value': 59}]}, {'date': 'Feb 15, 2021', 'timestamp': '1613347200', 'values': [{'query': 'BTC', 'value': '52', 'extracted_value': 52}]}, {'date': 'Feb 16, 2021', 'timestamp': '1613433600', 'values': [{'query': 'BTC', 'value': '55', 'extracted_value': 55}]}, {'date': 'Feb 17, 2021', 'timestamp': '1613520000', 'values': [{'query': 'BTC', 'value': '67', 'extracted_value': 67}]}, {'date': 'Feb 18, 2021', 'timestamp': '1613606400', 'values': [{'query': 'BTC', 'value': '57', 'extracted_value': 57}]}, {'date': 'Feb 19, 2021', 'timestamp': '1613692800', 'values': [{'query': 'BTC', 'value': '71', 'extracted_value': 71}]}, {'date': 'Feb 20, 2021', 'timestamp': '1613779200', 'values': [{'query': 'BTC', 'value': '97', 'extracted_value': 97}]}, {'date': 'Feb 21, 2021', 'timestamp': '1613865600', 'values': [{'query': 'BTC', 'value': '76', 'extracted_value': 76}]}, {'date': 'Feb 22, 2021', 'timestamp': '1613952000', 'values': [{'query': 'BTC', 'value': '85', 'extracted_value': 85}]}, {'date': 'Feb 23, 2021', 'timestamp': '1614038400', 'values': [{'query': 'BTC', 'value': '100', 'extracted_value': 100}]}, {'date': 'Feb 24, 2021', 'timestamp': '1614124800', 'values': [{'query': 'BTC', 'value': '84', 'extracted_value': 84}]}, {'date': 'Feb 25, 2021', 'timestamp': '1614211200', 'values': [{'query': 'BTC', 'value': '69', 'extracted_value': 69}]}, {'date': 'Feb 26, 2021', 'timestamp': '1614297600', 'values': [{'query': 'BTC', 'value': '53', 'extracted_value': 53}]}, {'date': 'Feb 27, 2021', 'timestamp': '1614384000', 'values': [{'query': 'BTC', 'value': '24', 'extracted_value': 24}]}, {'date': 'Feb 28, 2021', 'timestamp': '1614470400', 'values': [{'query': 'BTC', 'value': '59', 'extracted_value': 59}]}, {'date': 'Mar 1, 2021', 'timestamp': '1614556800', 'values': [{'query': 'BTC', 'value': '61', 'extracted_value': 61}]}]}}
#results = result_example # sample data to reduce number of API calls

search = GoogleSearch(params)
results = search.get_dict()

export_to_csv(results,filename)
print(filename + " succesfully saved.")




"""
## This code blocked by Google (Error 429)

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
"""