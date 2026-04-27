def add_development_stage(df):
    def stage(row):
        if row['life_expectancy'] > 75 and row['fertility'] < 2.1:
            return 'Developed'
        elif row['fertility'] > 4 or row['life_expectancy'] < 65:
            return 'Early Development'
        return 'Transition'

    df = df.copy()
    df['Stage'] = df.apply(stage, axis=1)
    return df