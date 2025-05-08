import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("../all_seasons_combined.csv", low_memory=False)
df['Date'] = pd.to_datetime(df['Date'])

# Extract season information
df['Season'] = df['Date'].apply(lambda x: f"{x.year}-{x.year + 1}" if x.month >= 8 else f"{x.year - 1}-{x.year}")

# Calculate the total goals scored by home and away teams each season
home_goals = df.groupby('Season')['FTHG'].sum()
away_goals = df.groupby('Season')['FTAG'].sum()

# Plotting the total goals scored by home and away teams
plt.figure(figsize=(12, 6))
plt.plot(home_goals, label='Home Goals', marker='o', color='coral', linestyle='-', linewidth=2, markersize=6)
plt.plot(away_goals, label='Away Goals', marker='o', color='dodgerblue', linestyle='-', linewidth=2, markersize=6)

# Customize the plot
plt.title('Total Goals Scored by Home and Away Teams per Season')
plt.xlabel('Season')
plt.ylabel('Total Goals Scored')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
