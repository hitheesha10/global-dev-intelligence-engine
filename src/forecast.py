from sklearn.linear_model import LinearRegression
import pandas as pd

def forecast(df, country):
    df = df[df['Country Name'] == country].dropna()

    results = {}

    for col in ['fertility', 'life_expectancy', 'population']:
        temp = df[['Year', col]].dropna()

        X = temp[['Year']]
        y = temp[col]

        model = LinearRegression()
        model.fit(X, y)

        future = pd.DataFrame({'Year': [2030]})
        pred = model.predict(future)[0]

        results[col] = round(pred, 2)

    return results