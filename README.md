In this project, we used historical NBA data from the 2016-2024 seasons to predict playoff team performance. The entire process involved data cleaning and pre-processing, feature engineering, exploratory data analysis (EDA), model training (random forest), and sentiment analysis.

Data Pre-Processing: 
We utilized pandas to obtain and clean the data for every NBA season between 2016 and 2024. The dataset includes statistics for each team, such as field goals made, turnovers, rebounds, and more. We performed extensive data wrangling to ensure the dataset was ready for analysis.

Exploratory Data Analysis (EDA): 
With the cleaned data, we conducted EDA using pandas and visualized trends using matplotlib and seaborn. This step helped identify key patterns and relationships between different team statistics that could be predictive of playoff success.

Predictive Modeling:
Using scikit-learn, we trained a Random Forest model on the historical data that we cleaned. The model was able to predict each team's wins in the playoffs with an impressive average RMSE of 1.1 wins. We then used our trained model to predict the 2025 NBA playoffs, and are looking forward to seeing how it performs. 

Sentiment Analysis: 
In addition to traditional team statistics, we wanted to incorporate fan sentiment into our model. To do this, we web scraped data from Reddit using Python, and then performed sentiment analysis with the NLTK library to gauge how fans were feeling about their team's performance. 

Future Improvements: 
We plan to continuously improve the model by adding more niche data points, refining the sentiment analysis process, and exploring other machine learning techniques. Our ultimate goal is to build a robust model that can accurately predict the outcome of future NBA playoff seasons.
