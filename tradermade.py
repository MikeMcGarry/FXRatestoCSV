import requests
import pandas as pd
from datetime import datetime

base_url = "https://tm-marketdata.com/api/v1"

endpoint = "/pandasDF"
secrets_file = 'secrets.txt'
currency_pairs_file = 'currency_pairs.txt'

secrets = open(secrets_file, "r")
api_token = secrets.read()
secrets.close()

currency_pairs = []

base_params = {
    "api_key": api_token,
    "start_date": "2018-09-19",
    "end_date": "2019-09-18",
    "format": "records",
    "fields": "close"
}

fx_rates = {}

currency_pairs = open(currency_pairs_file, "r")
currency_pairs_list = currency_pairs.read().splitlines()
currency_pairs.close()

responses = []
dates = []

for pair in currency_pairs_list:
    if len(pair) != 6:
        print (f"The pair of {pair} is too long at {len(pair)} characters. It must be two currency codes back to back for a total of 6 characters e.g. 'USDGBP'. Skipping this pair")
        continue

    print (f"Fetching rates from {base_params['start_date']} to {base_params['end_date']} for the currency pair {pair}")

    params = base_params.copy()
    params['currency'] = pair

    response = requests.get(base_url+endpoint, params)
    response_keyed = {}

    for record in response.json():
        response_keyed[record['date']] = record[pair]

    responses.append(response_keyed)
    dates += list(response_keyed.keys())

unique_dates = list(set(dates))
unique_dates.sort()

for response_keyed in responses:
    for date in unique_dates:
        if date not in response_keyed.keys():
            value = "MISSING"
        else:
            value = response_keyed[date]

        fx_rates.setdefault(date, []).append(value)

now = datetime.now()
fx_rates_df = pd.DataFrame(fx_rates, index=currency_pairs_list)
fx_rates_df.to_csv(f"./files/fx_rates_loaded_on_{now.day}_{now.month}_{now.year}.csv")




