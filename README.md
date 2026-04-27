🌍 Global Development Intelligence Engine
live link: https://global-dev-intelligence-engine.streamlit.app/
An AI-powered analytics platform that transforms raw World Bank datasets into interactive insights, simulations, and forecasts for global development trends.

🚀 What This Project Does
📊 Tracks population, fertility, and life expectancy across 190+ countries (1960–2016)
🎬 Visualizes global change using Gapminder-style animated dashboards
🌐 Integrates live World Bank API for real-time data updates
🧠 Predicts country income groups using machine learning
🔮 Forecasts future trends (2030 predictions) using regression models
⚙️ Enables what-if simulation to test policy scenarios
🧠 Key Features
🎬 Global Animation Dashboard

Interactive visualization showing how countries evolve over time:

Fertility ↓ vs Life Expectancy ↑
Bubble size = Population
Color-coded by region
🧠 AI Simulator

Simulate a country's future:

Input fertility, life expectancy, population
Predict income group classification
Evaluate development trajectory instantly
🔮 Forecast Engine (2030)

Uses historical trends to predict:

Future population
Life expectancy
Fertility rate
🌐 Live Data Integration

Fetches real-time indicators directly from:

World Bank API
🏗️ Tech Stack
Python
Pandas / NumPy
Scikit-learn
Plotly (interactive visuals)
Streamlit (UI & deployment)
⚙️ Architecture
Data Sources (CSV + API)
        ↓
Data Cleaning & Feature Engineering
        ↓
ML Models (Classification + Forecasting)
        ↓
Interactive Dashboard (Streamlit)
📸 Demo

👉 (Add your Streamlit link here)

🧪 How to Run Locally
git clone https://github.com/your-username/global-dev-intelligence.git
cd global-dev-intelligence

pip install -r requirements.txt
streamlit run app.py
💡 Key Insights
Fertility rates globally have declined significantly
Life expectancy has increased by 20+ years since 1960
Countries follow predictable development transitions
Population growth is stabilizing in developed regions
📈 Why This Project Matters

This project goes beyond visualization:

Combines data engineering + ML + product thinking
Demonstrates real-world decision intelligence systems
Simulates policy-level scenarios
🧠 Future Improvements
LLM-based country insights (auto-generated reports)
Advanced time-series models (ARIMA / LSTM)
Policy recommendation engine
