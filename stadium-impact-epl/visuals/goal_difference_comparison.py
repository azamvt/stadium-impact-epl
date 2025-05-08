import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("../all_seasons_combined.csv", low_memory=False)
df['Date'] = pd.to_datetime(df['Date'])

# Extract season information
df['Season'] = df['Date'].apply(lambda x: f"{x.year}-{x.year + 1}" if x.month >= 8 else f"{x.year - 1}-{x.year}")

# Calculate the goal difference (home goals - away goals) for each season
df['GoalDifference'] = df['FTHG'] - df['FTAG']

# Group by season and calculate the average goal difference per season
goal_difference_per_season = df.groupby('Season')['GoalDifference'].mean()

# Plotting the goal difference for each season
plt.figure(figsize=(12, 6))
plt.plot(goal_difference_per_season, label='Goal Difference (Home - Away)', marker='o', color='green', linestyle='-', linewidth=2, markersize=6)

# Customize the plot
plt.title('Average Goal Difference (Home - Away) per Season')
plt.xlabel('Season')
plt.ylabel('Average Goal Difference')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
