📌 Overview

This project uses historical NBA data (2016–2024) to predict playoff team performance and forecast outcomes for the 2025 NBA Playoffs.
We combined team statistics with fan sentiment from Reddit to capture both quantitative and qualitative drivers of playoff success.

🔧 Tech Stack

Python: pandas, NumPy, scikit-learn, NLTK

Visualization: matplotlib, seaborn

Modeling: Random Forest Regressor

Data Source: Basketball stats (2016–2024 seasons), Reddit fan posts

📊 Workflow
1. Data Preprocessing

Collected and cleaned team-level stats (field goals, turnovers, rebounds, etc.) for 2016–2024 seasons.

Performed extensive wrangling with pandas to ensure consistency across years.

2. Exploratory Data Analysis (EDA)

Analyzed trends in playoff success with pandas, matplotlib, and seaborn.

Identified correlations between key stats and playoff wins.

3. Predictive Modeling

Trained a Random Forest model on historical data.

Achieved average RMSE of 1.1 playoff wins on validation.

Applied model to predict 2025 playoff outcomes.

4. Sentiment Analysis

Scraped Reddit posts related to NBA teams.

Applied NLTK sentiment analysis to quantify fan sentiment.

Incorporated sentiment scores as model features to improve predictions.

🚀 Results

Robust predictive performance with RMSE ≈ 1.1 wins.

Captures both on-court performance and fan perception.

Currently forecasting the 2025 NBA Playoffs (results pending).

🔮 Future Improvements

Add niche data sources (injury reports, player tracking data).

Refine sentiment analysis with transformer-based NLP models.

Experiment with alternative ML models (XGBoost, neural networks).

Deploy as a web app for interactive playoff predictions.
