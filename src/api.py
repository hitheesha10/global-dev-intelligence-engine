import requests
import pandas as pd

INDICATORS = {
    "population": "SP.POP.TOTL",
    "fertility": "SP.DYN.TFRT.IN",
    "life_expectancy": "SP.DYN.LE00.IN"
}

def fetch_indicator(indicator_code):
    url = f"http://api.worldbank.org/v2/country/all/indicator/{indicator_code}?format=json&per_page=20000"
    res = requests.get(url).json()

    data = res[1]
    df = pd.DataFrame(data)

    df = df[['countryiso3code', 'date', 'value']]
    df.columns = ['Country Code', 'Year', 'value']

    df['Year'] = df['Year'].astype(int)
    return df

def get_live_data():
    pop = fetch_indicator(INDICATORS['population']).rename(columns={'value': 'population'})
    fert = fetch_indicator(INDICATORS['fertility']).rename(columns={'value': 'fertility'})
    life = fetch_indicator(INDICATORS['life_expectancy']).rename(columns={'value': 'life_expectancy'})

    df = pop.merge(fert, on=['Country Code', 'Year'])
    df = df.merge(life, on=['Country Code', 'Year'])

    return df