import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("../all_seasons_combined.csv", low_memory=False)
df['Date'] = pd.to_datetime(df['Date'])

# Extract season information
df['Season'] = df['Date'].apply(lambda x: f"{x.year}-{x.year + 1}" if x.month >= 8 else f"{x.year - 1}-{x.year}")

# Calculate goal difference per match (Home Goals - Away Goals)
df['Goal_Diff'] = df['FTHG'] - df['FTAG']

# Calculate average goal difference per season
season_goal_diff = df.groupby('Season')['Goal_Diff'].mean()

# Plotting
plt.figure(figsize=(12, 6))
season_goal_diff.plot(marker='s', color='mediumseagreen')
plt.title('Average Home Goal Difference by Season')
plt.xlabel('Season')
plt.ylabel('Average Goal Difference (Home - Away)')
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
