from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd

FEATURES = ['fertility', 'life_expectancy', 'population']

def train_model(df):
    df = df.dropna(subset=FEATURES + ['IncomeGroup'])

    X = df[FEATURES]
    y = df['IncomeGroup']

    le = LabelEncoder()
    y_enc = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y_enc, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=150, random_state=42)
    model.fit(X_train, y_train)

    acc = model.score(X_test, y_test)

    return model, le, acc


def predict(model, le, fertility, life, population):
    input_df = pd.DataFrame({
        'fertility': [fertility],
        'life_expectancy': [life],
        'population': [population]
    })

    # enforce feature order
    input_df = input_df[model.feature_names_in_]

    pred = model.predict(input_df)[0]
    return le.inverse_transform([pred])[0]