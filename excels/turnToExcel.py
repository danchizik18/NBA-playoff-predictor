import pandas as pd
# Replace 'your_file.csv' with the path to your CSV file
games_cleaned = pd.read_csv('../data/games_cleaned.csv')

league_leaders = pd.read_csv('../data/league_leaders_cleaned.csv')

player_stats = pd.read_csv('../data/player_stats_cleaned.csv')

playoff_results = pd.read_csv('../data/playoff_results.csv')

team_stats = pd.read_csv('../data/team_stats_cleaned.csv')



# Replace 'output.xlsx' with the desired Excel file name
games_cleaned.to_excel('games_cleaned.xlsx', index=False)
league_leaders.to_excel('league_leaders.xlsx', index=False)
player_stats.to_excel('player_stats.xlsx', index=False)
playoff_results.to_excel('playoff_results.xlsx', index=False)
team_stats.to_excel('team_stats.xlsx', index=False)