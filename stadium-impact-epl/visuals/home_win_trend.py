import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("../all_seasons_combined.csv", low_memory=False)
df['Date'] = pd.to_datetime(df['Date'])

# Extract season from the date (e.g., 2000-2001, 2001-2002, etc.)
df['Season'] = df['Date'].apply(lambda x: f"{x.year}-{x.year + 1}" if x.month >= 8 else f"{x.year - 1}-{x.year}")

# Determine match result
def match_result(row):
    if row['FTHG'] > row['FTAG']:
        return 'Home Win'
    elif row['FTHG'] < row['FTAG']:
        return 'Away Win'
    else:
        return 'Draw'

df['Result'] = df.apply(match_result, axis=1)

# Group by season and calculate home win ratio
season_home_win_ratio = df.groupby('Season')['Result'].apply(lambda x: (x == 'Home Win').mean())

# Plotting
plt.figure(figsize=(12, 6))
season_home_win_ratio.plot(marker='o', color='dodgerblue')
plt.title('Home Win Rate by Season')
plt.xlabel('Season')
plt.ylabel('Home Win Rate')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
