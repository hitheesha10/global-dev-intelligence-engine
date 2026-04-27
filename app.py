import streamlit as st
import pandas as pd
import plotly.express as px

from src.clean_data import build_clean_dataset
from src.features import add_development_stage
from src.models import train_model, predict
from src.forecast import forecast
from src.api import get_live_data

st.set_page_config(page_title="Global Dev Intelligence", layout="wide")

# ---------------- HEADER ---------------- #
st.title("🌍 Global Development Intelligence Engine")
st.caption("AI-powered analytics for population, fertility & life expectancy (1960–2016 + Live Data)")

# ---------------- LOAD DATA ---------------- #
@st.cache_data
def load_data():
    df = build_clean_dataset(
        "data/country_population.csv",
        "data/fertility_rate.csv",
        "data/life_expectancy.csv",
        "data/metadata_country.csv"
    )
    df = add_development_stage(df)
    return df

df = load_data()

# ---------------- KPI ROW ---------------- #
col1, col2, col3 = st.columns(3)

col1.metric("🌎 Countries", df['Country Name'].nunique())
col2.metric("📅 Years Covered", f"{df['Year'].min()} - {df['Year'].max()}")
col3.metric("📊 Data Points", len(df))

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("⚙️ Controls")

selected_countries = st.sidebar.multiselect(
    "Select Countries",
    sorted(df['Country Name'].unique()),
    default=["India", "United States"]
)

year_range = st.sidebar.slider("Year Range", 1960, 2016, (1990, 2016))

# Filter
filtered = df[df['Year'].between(*year_range)]
if selected_countries:
    filtered = filtered[filtered['Country Name'].isin(selected_countries)]

# ---------------- TABS ---------------- #
tab1, tab2, tab3, tab4 = st.tabs([
    "🎬 Global Animation",
    "📊 Country Analysis",
    "🧠 AI Simulator",
    "🔮 Future Forecast"
])

# ---------------- TAB 1 ---------------- #
with tab1:
    st.subheader("Global Development Over Time")

    fig = px.scatter(
        filtered,
        x="fertility",
        y="life_expectancy",
        animation_frame="Year",
        animation_group="Country Code",
        size="population",
        color="Region",
        hover_name="Country Name",
        log_x=True,
        size_max=60
    )

    st.plotly_chart(fig, width='stretch')

# ---------------- TAB 2 ---------------- #
with tab2:
    st.subheader("Country Trends")

    metric = st.selectbox("Select Metric", ["population", "fertility", "life_expectancy"])

    fig2 = px.line(
        filtered,
        x="Year",
        y=metric,
        color="Country Name",
        title=f"{metric} Trend"
    )

    st.plotly_chart(fig2, width='stretch')

    # Comparison Insight
    st.subheader("📌 Insight")
    st.info(
        "Countries transitioning to lower fertility often show rapid life expectancy growth — indicating healthcare and economic improvements."
    )

# ---------------- TAB 3 ---------------- #
with tab3:
    st.subheader("What-if Country Simulator")

    model, le, acc = train_model(df)

    col1, col2, col3 = st.columns(3)

    fertility = col1.slider("Fertility", 1.0, 7.0, 2.5)
    life = col2.slider("Life Expectancy", 40, 85, 70)
    population = col3.number_input("Population", value=50000000)

    if st.button("Predict Income Group"):
        result = predict(model, le, fertility, life, population)

        st.success(f"Predicted Income Group: {result}")
        st.metric("Model Accuracy", f"{round(acc*100,2)}%")

# ---------------- TAB 4 ---------------- #
with tab4:
    st.subheader("2030 Forecast Engine")

    country = st.selectbox("Select Country", df['Country Name'].unique())

    if st.button("Generate Forecast"):
        result = forecast(df, country)

        c1, c2, c3 = st.columns(3)

        c1.metric("Fertility (2030)", result['fertility'])
        c2.metric("Life Expectancy (2030)", result['life_expectancy'])
        c3.metric("Population (2030)", result['population'])

        st.success("Prediction based on historical trend modeling")

# ---------------- LIVE DATA ---------------- #
st.divider()
st.subheader("🌐 Live World Bank Data")

if st.button("Fetch Live Data"):
    live_df = get_live_data()
    st.success("Live data loaded")
    st.dataframe(live_df.head(), width='stretch')

# ---------------- FOOTER ---------------- #
st.markdown("---")
st.caption("Built with Machine Learning, Real-time APIs & Interactive Visualization")