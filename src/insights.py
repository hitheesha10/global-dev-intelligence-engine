def global_insight(df):
    start = df[df['Year']==1960]
    end = df[df['Year']==2016]

    return f"""
🌍 Global Shift:
- Fertility dropped from {start['fertility'].mean():.2f} → {end['fertility'].mean():.2f}
- Life expectancy increased from {start['life_expectancy'].mean():.2f} → {end['life_expectancy'].mean():.2f}

➡️ Massive global development transition
"""