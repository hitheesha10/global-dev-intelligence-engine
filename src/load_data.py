import pandas as pd

def load_raw_data(pop_path, fert_path, life_path, meta_path):
    return (
        pd.read_csv(pop_path),
        pd.read_csv(fert_path),
        pd.read_csv(life_path),
        pd.read_csv(meta_path)
    )

def melt_world_bank(df, value_name):
    years = [str(y) for y in range(1960, 2017)]

    df = pd.melt(
        df,
        id_vars=['Country Name', 'Country Code'],
        value_vars=years,
        var_name='Year',
        value_name=value_name
    )

    df['Year'] = df['Year'].astype(int)
    return df

def prepare_all_data(pop, fert, life, meta):
    pop = melt_world_bank(pop, 'population')
    fert = melt_world_bank(fert, 'fertility')
    life = melt_world_bank(life, 'life_expectancy')

    df = meta.merge(pop, on='Country Code')
    df = df.merge(fert, on=['Country Name', 'Country Code', 'Year'])
    df = df.merge(life, on=['Country Name', 'Country Code', 'Year'])

    df = df[['Country Name','Country Code','Region','IncomeGroup',
             'Year','population','fertility','life_expectancy']]

    df = df.dropna().sort_values(['Country Name','Year'])

    return df